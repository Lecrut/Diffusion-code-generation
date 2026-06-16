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
    print(f"{time_a} to {time_b}: {result1}")
    time_c = "23:00"
    time_d = "01:00"
    result2 = time_difference_hours(time_c, time_d)
    print(f"{time_c} to {time_d}: {result2}")
    time_e = "08:00"
    time_f = "09:00"
    result3 = time_difference_hours(time_e, time_f)
    print(f"{time_e} to {time_f}: {result3}")
    time_g = "15:00"
    time_h = "10:00"
    result4 = time_difference_hours(time_g, time_h)
    print(f"{time_g} to {time_h}: {result4}")