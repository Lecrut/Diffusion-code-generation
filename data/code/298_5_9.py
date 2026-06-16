import datetime
def time_difference(time1_str, time2_str):
    time_format = "%H:%M"
    time1 = datetime.datetime.strptime(time1_str, time_format)
    time2 = datetime.datetime.strptime(time2_str, time_format)
    if time2 > time1:
        diff = (time2 - time1).total_seconds() / 60
        return int(diff)
    else:
        raise ValueError("Second time is not chronologically after the first time")
if __name__ == '__main__':
    try:
        t1 = "10:30"
        t2 = "11:15"
        result = time_difference(t1, t2)
        print(f"Difference between {t1} and {t2}: {result} minutes")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        t1 = "14:00"
        t2 = "13:59"
        result = time_difference(t1, t2)
        print(f"Difference between {t1} and {t2}: {result} minutes")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        t1 = "09:00"
        t2 = "09:00"
        result = time_difference(t1, t2)
        print(f"Difference between {t1} and {t2}: {result} minutes")
    except ValueError as e:
        print(f"Error: {e}")