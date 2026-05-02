import datetime
def time_difference_seconds(time_str1, time_str2):
    time1 = datetime.datetime.strptime(time_str1, "%H:%M:%S").time()
    time2 = datetime.datetime.strptime(time_str2, "%H:%M:%S").time()
    total_seconds1 = time1.hour * 3600 + time1.minute * 60 + time1.second
    total_seconds2 = time2.hour * 3600 + time2.minute * 60 + time2.second
    return abs(total_seconds1 - total_seconds2)
if __name__ == '__main__':
    time1 = "10:30:00"
    time2 = "14:45:15"
    difference = time_difference_seconds(time1, time2)
    print(difference)