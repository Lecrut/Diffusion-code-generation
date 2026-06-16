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
    time1_a = "01:00"
    time2_a = "03:30"
    result_a = calculate_duration(time1_a, time2_a)
    print(f"{time1_a} to {time2_a}: {result_a} minutes")
    time1_b = "23:00"
    time2_b = "01:00"
    result_b = calculate_duration(time1_b, time2_b)
    print(f"{time1_b} to {time2_b}: {result_b} minutes")
    time1_c = "10:00"
    time2_c = "10:00"
    result_c = calculate_duration(time1_c, time2_c)
    print(f"{time1_c} to {time2_c}: {result_c} minutes")
    time1_d = "08:00"
    time2_d = "17:00"
    result_d = calculate_duration(time1_d, time2_d)
    print(f"{time1_d} to {time2_d}: {result_d} minutes")