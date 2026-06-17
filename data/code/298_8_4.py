import datetime
def calculate_duration(time_str1, time_str2):
    time1 = datetime.datetime.strptime(time_str1, '%H:%M')
    time2 = datetime.datetime.strptime(time_str2, '%H:%M')
    time1_total_minutes = time1.hour * 60 + time1.minute
    time2_total_minutes = time2.hour * 60 + time2.minute
    if time2_total_minutes >= time1_total_minutes:
        duration_minutes = time2_total_minutes - time1_total_minutes
    else:
        duration_minutes = (24 * 60) - time1_total_minutes + time2_total_minutes
    return duration_minutes
if __name__ == '__main__':
    time_a = "01:30"
    time_b = "05:45"
    result1 = calculate_duration(time_a, time_b)
    print(f"{result1}")
    time_c = "23:00"
    time_d = "01:00"
    result2 = calculate_duration(time_c, time_d)
    print(f"{result2}")
    time_e = "10:00"
    time_f = "12:30"
    result3 = calculate_duration(time_e, time_f)
    print(f"{result3}")