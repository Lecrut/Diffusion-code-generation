from datetime import datetime

def calculate_time_elapsed(start_time, end_time):
    time_difference = end_time - start_time
    hours_elapsed = time_difference.total_seconds() / 3600
    return hours_elapsed

if __name__ == '__main__':
    start_datetime = datetime(2023, 10, 1, 12, 0, 0)
    end_datetime = datetime(2023, 10, 1, 14, 30, 0)
    elapsed_hours = calculate_time_elapsed(start_datetime, end_datetime)
    print(f"Time elapsed: {elapsed_hours} hours")