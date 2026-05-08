import datetime
import pytz
def calculate_elapsed_time():
    now_utc = datetime.datetime.now(pytz.utc)
    start_of_day_utc = now_utc.replace(hour=0, minute=0, second=0, microsecond=0)
    elapsed_time = now_utc - start_of_day_utc
    print(f"Current time (UTC): {now_utc}")
    print(f"Start of today (UTC): {start_of_day_utc}")
    print(f"Time elapsed today: {elapsed_time}")
if __name__ == '__main__':
    calculate_elapsed_time()