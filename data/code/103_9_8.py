import datetime
import time
if __name__ == '__main__':
    now_utc = datetime.datetime.utcnow()
    print(f"Current UTC time: {now_utc}")
    today_start = now_utc.replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = now_utc.replace(hour=23, minute=59, second=59, microsecond=999999)
    print(f"Start of today (UTC): {today_start}")
    print(f"End of today (UTC): {today_end}")
    time_today_seconds = (today_end - today_start).total_seconds()
    print(f"Total seconds in a day: {time_today_seconds}")
    print(f"Exact time elapsed today (in seconds): {time_today_seconds}")