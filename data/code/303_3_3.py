from datetime import datetime
def calculate_time_elapsed(time_strings):
    if not time_strings:
        return 0
    time_objects = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in time_strings]
    first_time = min(time_objects)
    last_time = max(time_objects)
    time_difference = last_time - first_time
    return time_difference.total_seconds()
if __name__ == '__main__':
    sample_times = [
        "2023-01-01 10:00:00",
        "2023-01-01 11:30:00",
        "2023-01-02 09:00:00"
    ]
    elapsed_time = calculate_time_elapsed(sample_times)
    print(elapsed_time)