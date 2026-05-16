import datetime
def calculate_elapsed_hours(time_str1, time_str2):
    try:
        time1 = datetime.datetime.strptime(time_str1, '%H:%M:%S')
        time2 = datetime.datetime.strptime(time_str2, '%H:%M:%S')
        diff = abs(time1 - time2)
        return diff.total_seconds() / 3600.0
    except ValueError:
        return float('nan')
if __name__ == '__main__':
    t1 = "01:00:00"
    t2 = "05:30:00"
    result1 = calculate_elapsed_hours(t1, t2)
    print(f"{t1} and {t2}: {result1}")
    t3 = "10:00:00"
    t4 = "10:00:00"
    result2 = calculate_elapsed_hours(t3, t4)
    print(f"{t3} and {t4}: {result2}")
    t5 = "23:59:59"
    t6 = "00:00:01"
    result3 = calculate_elapsed_hours(t5, t6)
    print(f"{t5} and {t6}: {result3}")
    t7 = "99:99:99"
    t8 = "10:00:00"
    result4 = calculate_elapsed_hours(t7, t8)
    print(f"{t7} and {t8}: {result4}")
    t9 = "invalid"
    t10 = "10:00:00"
    result5 = calculate_elapsed_hours(t9, t10)
    print(f"{t9} and {t10}: {result5}")