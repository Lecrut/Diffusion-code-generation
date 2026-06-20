import datetime

def parse_time(time_str):
    try:
        return datetime.datetime.strptime(time_str, '%H:%M:%S')
    except ValueError:
        raise ValueError("Invalid time format. Please use 'HH:MM:SS'")

def calculate_elapsed_hours(time_str1, time_str2):
    time1 = parse_time(time_str1)
    time2 = parse_time(time_str2)
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