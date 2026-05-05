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
    t1 = "01:00:00"
    t2 = "03:30:00"
    result1 = calculate_elapsed_hours(t1, t2)
    print(f"Difference between {t1} and {t2}: {result1} hours")
    t3 = "10:15:30"
    t4 = "09:45:00"
    result2 = calculate_elapsed_hours(t3, t4)
    print(f"Difference between {t3} and {t4}: {result2} hours")
    t5 = "23:59:59"
    t6 = "00:00:01"
    result3 = calculate_elapsed_hours(t5, t6)
    print(f"Difference between {t5} and {t6}: {result3} hours")
    t7 = "99:99:99"
    t8 = "01:00:00"
    result4 = calculate_elapsed_hours(t7, t8)
    print(f"Difference between {t7} and {t8}: {result4} hours (Error handling test)")