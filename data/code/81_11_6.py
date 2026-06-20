import datetime

def calculate_elapsed_hours(time1, time2):
    try:
        dt1 = datetime.datetime.strptime(time1, '%H:%M:%S')
        dt2 = datetime.datetime.strptime(time2, '%H:%M:%S')
        diff = abs(dt1 - dt2)
        return diff.total_seconds() / 3600.0
    except ValueError:
        return float('nan')

if __name__ == '__main__':
    time_a = "01:00:00"
    time_b = "05:30:00"
    result1 = calculate_elapsed_hours(time_a, time_b)
    print(f"Difference between {time_a} and {time_b}: {result1} hours")
    
    time_c = "10:15:30"
    time_d = "10:15:30"
    result2 = calculate_elapsed_hours(time_c, time_d)
    print(f"Difference between {time_c} and {time_d}: {result2} hours")