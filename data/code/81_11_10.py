import datetime

def validate_times(time_str1, time_str2):
    time_format = '%H:%M:%S'
    try:
        datetime.datetime.strptime(time_str1, time_format)
        datetime.datetime.strptime(time_str2, time_format)
    except ValueError:
        raise ValueError("Both inputs must be in the format HH:MM:SS")

def calculate_elapsed_hours(time_str1, time_str2):
    validate_times(time_str1, time_str2)
    time1 = datetime.datetime.strptime(time_str1, '%H:%M:%S')
    time2 = datetime.datetime.strptime(time_str2, '%H:%M:%S')
    diff = abs(time1 - time2)
    return diff.total_seconds() / 3600.0

if __name__ == '__main__':
    time_a = "01:00:00"
    time_b = "05:30:00"
    result1 = calculate_elapsed_hours(time_a, time_b)
    print(f"Difference between {time_a} and {time_b}: {result1} hours")
    time_c = "10:15:30"
    time_d = "10:15:30"
    result2 = calculate_elapsed_hours(time_c, time_d)
    print(f"Difference between {time_c} and {time_d}: {result2} hours")