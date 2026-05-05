import datetime
def calculate_elapsed_hours(start_time_str, end_time_str):
    start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
    time_difference = end_time - start_time
    elapsed_seconds = time_difference.total_seconds()
    elapsed_hours = elapsed_seconds / 3600.0
    return elapsed_hours
if __name__ == '__main__':
    start = "2023-10-27 09:00:00"
    end = "2023-10-27 17:30:00"
    result = calculate_elapsed_hours(start, end)
    print(result)