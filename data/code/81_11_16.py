import datetime

def calculate_elapsed_hours(time_str1, time_str2):
    try:
        time_format = '%H:%M:%S'
        time1 = datetime.datetime.strptime(time_str1, time_format)
        time2 = datetime.datetime.strptime(time_str2, time_format)
        diff = abs(time1 - time2)
        return diff.total_seconds() / 3600.0
    except ValueError:
        return float('nan')

if __name__ == '__main__':
    times = {
        'time_a': "01:00:00",
        'time_b': "05:30:00",
        'time_c': "10:15:30",
        'time_d': "10:15:30"
    }
    
    result1 = calculate_elapsed_hours(times['time_a'], times['time_b'])
    print(f"Difference between {times['time_a']} and {times['time_b']}: {result1} hours")
    
    result2 = calculate_elapsed_hours(times['time_c'], times['time_d'])
    print(f"Difference between {times['time_c']} and {times['time_d']}: {result2} hours")