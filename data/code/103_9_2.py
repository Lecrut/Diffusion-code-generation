import datetime
import time
if __name__ == '__main__':
    now_utc = datetime.datetime.utcnow()
    print(f"Current UTC time: {now_utc}")
    start_of_day_utc = now_utc.replace(hour=0, minute=0, second=0, microsecond=0)
    time_elapsed_seconds = (now_utc - start_of_day_utc).total_seconds()
    print(f"Time elapsed today in seconds: {time_elapsed_seconds}")
    current_timestamp = time.time()
    start_of_day_timestamp = start_of_day_utc.timestamp()
    time_elapsed_since_epoch = current_timestamp - start_of_day_timestamp
    print(f"Time elapsed since start of day (epoch based): {time_elapsed_since_epoch}")