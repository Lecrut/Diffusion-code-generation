import datetime
def calculate_duration(time_str1, time_str2):
    time1 = datetime.datetime.strptime(time_str1, '%H:%M')
    time2 = datetime.datetime.strptime(time_str2, '%H:%M')
    if time2 >= time1:
        duration = time2 - time1
    else:
        duration = (time2 + datetime.timedelta(days=1)) - time1
    return duration
if __name__ == '__main__':
    time_a = "01:00"
    time_b = "03:30"
    result1 = calculate_duration(time_a, time_b)
    print(f"Duration between {time_a} and {time_b}: {result1}")
    time_c = "23:00"
    time_d = "01:00"
    result2 = calculate_duration(time_c, time_d)
    print(f"Duration between {time_c} and {time_d}: {result2}")
    time_e = "10:00"
    time_f = "15:00"
    result3 = calculate_duration(time_e, time_f)
    print(f"Duration between {time_e} and {time_f}: {result3}")
    time_g = "08:00"
    time_h = "20:00"
    result4 = calculate_duration(time_g, time_h)
    print(f"Duration between {time_g} and {time_h}: {result4}")