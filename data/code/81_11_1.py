import datetime
def calculate_elapsed_hours(time_str1, time_str2):
    time_format = '%H:%M:%S'
    try:
        time1 = datetime.datetime.strptime(time_str1, time_format)
        time2 = datetime.datetime.strptime(time_str2, time_format)
        diff = abs(time1 - time2)
        return diff.total_seconds() / 3600.0
    except ValueError:
        return float('nan')
if __name__ == '__main__':
    time_a = "01:00:00"
    time_b = "03:30:00"
    result1 = calculate_elapsed_hours(time_a, time_b)
    print(f"Difference between {time_a} and {time_b}: {result1} hours")
    time_c = "10:15:30"
    time_d = "10:15:30"
    result2 = calculate_elapsed_hours(time_c, time_d)
    print(f"Difference between {time_c} and {time_d}: {result2} hours")
    time_e = "23:59:59"
    time_f = "00:00:01"
    result3 = calculate_elapsed_hours(time_e, time_f)
    print(f"Difference between {time_e} and {time_f}: {result3} hours")
    time_g = "invalid_time"
    time_h = "01:00:00"
    result4 = calculate_elapsed_hours(time_g, time_h)
    print(f"Difference between {time_g} and {time_h}: {result4} hours")