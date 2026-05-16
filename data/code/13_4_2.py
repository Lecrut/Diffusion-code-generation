import datetime
def time_difference_seconds(time_str1, time_str2):
    time1 = datetime.datetime.strptime(time_str1, "%H:%M:%S").time()
    time2 = datetime.datetime.strptime(time_str2, "%H:%M:%S").time()
    seconds1 = time1.hour * 3600 + time1.minute * 60 + time1.second
    seconds2 = time2.hour * 3600 + time2.minute * 60 + time2.second
    return abs(seconds1 - seconds2)
if __name__ == '__main__':
    time_a = "10:00:00"
    time_b = "10:05:30"
    diff1 = time_difference_seconds(time_a, time_b)
    print(f"{time_a} and {time_b}: {diff1} seconds")
    time_c = "01:00:00"
    time_d = "00:59:59"
    diff2 = time_difference_seconds(time_c, time_d)
    print(f"{time_c} and {time_d}: {diff2} seconds")
    time_e = "23:59:59"
    time_f = "00:00:01"
    diff3 = time_difference_seconds(time_e, time_f)
    print(f"{time_e} and {time_f}: {diff3} seconds")