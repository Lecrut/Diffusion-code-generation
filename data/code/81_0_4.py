import datetime

def calculate_elapsed_hours(start_time_str: str, end_time_str: str) -> float:
    start_time = datetime.datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
    if end_time < start_time:
        end_time += datetime.timedelta(days=1)
    time_difference = end_time - start_time
    elapsed_seconds = time_difference.total_seconds()
    elapsed_hours = elapsed_seconds / 3600.0
    return elapsed_hours
if __name__ == '__main__':
    start = '2023-10-05 22:00:00'
    end = '2023-10-06 04:30:00'
    result = calculate_elapsed_hours(start, end)
    print(result)