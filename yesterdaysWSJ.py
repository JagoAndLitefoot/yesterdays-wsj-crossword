import webbrowser
import datetime

is_monday = datetime.datetime.today().weekday() == 0
if is_monday:
    target = datetime.date.today() - datetime.timedelta(2)
else:
    target = datetime.date.today() - datetime.timedelta(1)
url = "http://herbach.dnsalias.com/wsj/wsj%s.puz" % target.strftime('%y%m%d')
webbrowser.open(url, new=2, autoraise=False)

# by jagoandlitefoot / jenna lafleur
# 2017-07-01