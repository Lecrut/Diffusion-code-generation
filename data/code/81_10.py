import datetime
import pytz
if __name__ == '__main__':
    start_time_str = "2023-01-01 10:00:00"
    end_time_str = "2023-01-03 14:30:00"
    start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
    try:
        elapsed_time = end_time - start_time
        total_seconds = elapsed_time.total_seconds()
        total_hours = total_seconds / 3600.0
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")
        print(f"Elapsed Time in Hours: {total_hours}")
    except Exception as e:
        print(f"An error occurred: {e}")