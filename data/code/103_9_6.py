import datetime
import pytz
if __name__ == '__main__':
    now_utc = datetime.datetime.now(pytz.utc)
    print(f"Current time in UTC: {now_utc}")
    today_start_utc = now_utc.replace(hour=0, minute=0, second=0, microsecond=0)
    print(f"Start of today in UTC: {today_start_utc}")
    time_elapsed_today = now_utc - today_start_utc
    print(f"Time elapsed today (timedelta): {time_elapsed_today}")
    total_seconds = time_elapsed_today.total_seconds()
    print(f"Total seconds elapsed today: {total_seconds}")
    print(f"Time elapsed today in hours: {time_elapsed_today.total_seconds() / 3600}")
    print(f"Time elapsed today in days: {time_elapsed_today.total_seconds() / (3600 * 24)}")