# https://ithelp.ithome.com.tw/articles/10218874?sc=pt
# from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import time
import urllib.request

sched = BackgroundScheduler()

# @sched.scheduled_job('interval', day_of_week='mon-fri', minutes=20)
@sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/20')
def timed_job():
    url = "https://van-linebot.herokuapp.com/"
    conn = urllib.request.urlopen(url)
    # cost down aonther app
    # url2 = "https://mingchang.herokuapp.com/home/"
    # conn = urllib.request.urlopen(url2)
    today = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(today, 'This job is run every work day twenty minutes.')

sched.start()