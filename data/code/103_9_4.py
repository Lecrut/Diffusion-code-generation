import datetime
import time
if __name__ == '__main__':
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    print(f"Current time in UTC: {now_utc}")
    start_of_day_utc = now_utc.replace(hour=0, minute=0, second=0, microsecond=0)
    time_elapsed_today_utc = now_utc - start_of_day_utc
    print(f"Time elapsed today (UTC): {time_elapsed_today_utc}")
    local_time = datetime.datetime.now()
    start_of_day_local = local_time.replace(hour=0, minute=0, second=0, microsecond=0)
    time_elapsed_today_local = local_time - start_of_day_local
    print(f"Current local time: {local_time}")
    print(f"Time elapsed today (Local): {time_elapsed_today_local}")