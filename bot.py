import os, yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN = os.environ["TOKEN"]
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola! Soy DIOSITO MUSIC 
Mandame el nombre de cualquier cancion")
async def bajar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q=update.message.text
    if q.startswith("/"): return
    await update.message.reply_text(f"Buscando: {q}")
    try:
        opts={"format":"bestaudio/best","outtmpl":"%(title)s.%(ext)s","postprocessors":[{"key":"FFmpegExtractAudio","preferredcodec":"mp3","preferredquality":"192"}],"quiet":True,"noplaylist":True}
        with yt_dlp.YoutubeDL(opts) as ydl:
            info=ydl.extract_info(f"ytsearch1:{q}", download=True)
            title=info["entries"][0]["title"]
            file=ydl.prepare_filename(info["entries"][0]).rsplit(".",1)[0]+".mp3"
            await update.message.reply_audio(audio=open(file,"rb"), title=title)
            import os as _o; _o.remove(file)
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")
app=ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, bajar))
print("DIOSITO MUSIC PRENDIDO 24/7")
app.run_polling()
