import datetime
def calculate_time_difference_hours(start_time_str, end_time_str):
    start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
    time_difference = end_time - start_time
    return time_difference.total_seconds() / 3600.0
if __name__ == '__main__':
    start = "2023-01-01 10:00:00"
    end = "2023-01-31 15:30:00"
    elapsed_hours = calculate_time_difference_hours(start, end)
    print(elapsed_hours)