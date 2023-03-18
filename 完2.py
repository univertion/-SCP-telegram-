import requests
import random
import time
from bs4 import BeautifulSoup
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import numpy as np

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    n=(random.randint(101,3000))
    url=('http://scp-wiki-cn.wikidot.com/scp-')
    response = requests.get(url+str(n))
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find(id='page-content').get_text()
    
    
    await context.bot.send_message(chat_id=608152463, text=content)

if __name__ == '__main__':
    
    application = ApplicationBuilder().token('5930787327:AAFApKXgAdqgf-M7as9EVWyPBCshF3fFbfw').build()
    
    start_handler = CommandHandler('randscp', start)
    application.add_handler(start_handler)
    
    application.run_polling()
