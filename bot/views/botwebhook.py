from django.http import HttpResponse
from telegram import Update
from bot.control.update import run_bot
import json
from django.views.decorators.csrf import csrf_exempt
from config import DEBUG
from time import sleep
from datetime import datetime
import asyncio
from app.models import *
from gevent import spawn
from django.db import close_old_connections
from psycogreen.gevent import patch_psycopg

@csrf_exempt
def bot_webhook(request, bot_token):
    dp, updater = run_bot(bot_token)
    update = Update.de_json(json.loads(request.body.decode("utf-8")), dp.bot)
    dp.update_persistence(update)
    dp.process_update(update)

    return HttpResponse("Bot started!")

def create_test():
    Test.objects.create(title = "lalal")
    close_old_connections()


def demo(request):
    # spawn(create_test)
    # start = datetime.now().strftime("%H:%M:%S")
    # await asyncio.sleep(5)
    # await asyncio.sleep(5)
    sleep(4)
    # end = datetime.now().strftime("%H:%M:%S:%f")
    # return HttpResponse(f'{start} - {end}')
    return HttpResponse('OK')



# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# result = loop.run_until_complete(bot_webhook(request))