from datetime import datetime
def calculate_total_elapsed_time(time_strings):
    if not time_strings:
        return 0
    time_objects = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in time_strings]
    if not time_objects:
        return 0
    first_time = min(time_objects)
    last_time = max(time_objects)
    time_difference = last_time - first_time
    return time_difference.total_seconds()
if __name__ == '__main__':
    sample_times = [
        "2023-10-26 10:00:00",
        "2023-10-26 11:30:00",
        "2023-10-25 09:00:00",
        "2023-10-27 15:45:00"
    ]
    elapsed_time = calculate_total_elapsed_time(sample_times)
    print(elapsed_time)