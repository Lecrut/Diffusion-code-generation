import datetime
def time_difference_hours(time1_str, time2_str):
    time1 = datetime.datetime.strptime(time1_str, "%H:%M")
    time2 = datetime.datetime.strptime(time2_str, "%H:%M")
    if time1 > time2:
        time2 += datetime.timedelta(days=1)
    difference = time1 - time2
    return difference.total_seconds() / 3600
if __name__ == '__main__':
    time_a = "10:00"
    time_b = "14:00"
    result1 = time_difference_hours(time_a, time_b)
    print(f"Difference between {time_a} and {time_b}: {result1}")
    time_c = "23:00"
    time_d = "01:00"
    result2 = time_difference_hours(time_c, time_d)
    print(f"Difference between {time_c} and {time_d}: {result2}")
    time_e = "08:00"
    time_f = "16:00"
    result3 = time_difference_hours(time_e, time_f)
    print(f"Difference between {time_e} and {time_f}: {result3}")