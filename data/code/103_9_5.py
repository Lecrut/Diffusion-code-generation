import datetime
import time
if __name__ == '__main__':
    now_utc = datetime.datetime.utcnow()
    print(f"Current UTC time: {now_utc}")
    start_of_day_utc = now_utc.replace(hour=0, minute=0, second=0, microsecond=0)
    time_elapsed_seconds = (now_utc - start_of_day_utc).total_seconds()
    print(f"Time elapsed today (since midnight UTC): {time_elapsed_seconds:.3f} seconds")
    local_now = datetime.datetime.now()
    print(f"Current local time: {local_now}")
    start_of_day_local = local_now.replace(hour=0, minute=0, second=0, microsecond=0)
    local_time_elapsed_seconds = (local_now - start_of_day_local).total_seconds()
    print(f"Time elapsed today (since midnight local): {local_time_elapsed_seconds:.3f} seconds")