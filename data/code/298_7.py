import datetime
if __name__ == '__main__':
    time_str1 = "09:30"
    time_str2 = "17:45"
    time1 = datetime.datetime.strptime(time_str1, "%H:%M")
    time2 = datetime.datetime.strptime(time_str2, "%H:%M")
    difference = time2 - time1
    total_minutes = difference.total_seconds() / 60
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)
    print(f"Time difference: {hours} hours and {minutes} minutes")