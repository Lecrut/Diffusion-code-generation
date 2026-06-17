import datetime
def calculate_duration(time_str1, time_str2):
    time1 = datetime.datetime.strptime(time_str1, '%H:%M').time()
    time2 = datetime.datetime.strptime(time_str2, '%H:%M').time()
    if time2 >= time1:
        duration = datetime.timedelta(hours=time2.hour - time1.hour, minutes=time2.minute - time1.minute)
    else:
        duration = datetime.timedelta(days=1, hours=24 + time2.hour - time1.hour, minutes=time2.minute - time1.minute)
    return duration
if __name__ == '__main__':
    t1 = "01:00"
    t2 = "03:30"
    result1 = calculate_duration(t1, t2)
    print(f"Duration between {t1} and {t2}: {result1}")
    t3 = "23:00"
    t4 = "01:00"
    result2 = calculate_duration(t3, t4)
    print(f"Duration between {t3} and {t4}: {result2}")
    t5 = "10:00"
    t6 = "15:00"
    result3 = calculate_duration(t5, t6)
    print(f"Duration between {t5} and {t6}: {result3}")