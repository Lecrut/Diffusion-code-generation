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
    print(f"Total seconds in the day: {time_today_seconds}")
    elapsed_seconds_today = (now_utc - today_start).total_seconds()
    print(f"Time elapsed today (since midnight UTC): {elapsed_seconds_today} seconds")
    local_now = datetime.datetime.now()
    local_today_start = local_now.replace(hour=0, minute=0, second=0, microsecond=0)
    local_elapsed_seconds = (local_now - local_today_start).total_seconds()
    print(f"Time elapsed today (since local midnight): {local_elapsed_seconds} seconds")