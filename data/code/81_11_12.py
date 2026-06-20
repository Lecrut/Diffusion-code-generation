import datetime

def calculate_elapsed_hours(time_str1, time_str2):
    time_format = '%H:%M:%S'
    try:
        time1 = datetime.datetime.strptime(time_str1, time_format)
        time2 = datetime.datetime.strptime(time_str2, time_format)
        diff = abs(time2 - time1)
        return diff.total_seconds() / 3600.0
    except ValueError:
        return float('nan')

if __name__ == '__main__':
    start_time = "08:00:00"
    end_time = "17:45:00"
    duration = calculate_elapsed_hours(start_time, end_time)
    print(f"Duration from {start_time} to {end_time}: {duration} hours")

    same_times = "12:30:00"
    result = calculate_elapsed_hours(same_times, same_times)
    print(f"Difference between {same_times} and itself: {result} hours")