import datetime
def time_difference(time1_str, time2_str):
    time_format = "%H:%M"
    time1 = datetime.datetime.strptime(time1_str, time_format)
    time2 = datetime.datetime.strptime(time2_str, time_format)
    if time2 > time1:
        diff = (time2 - time1).total_seconds() / 60
        return int(diff)
    elif time2 < time1:
        raise ValueError("Second time is not chronologically after the first time.")
    else:
        raise ValueError("The two times are identical.")
if __name__ == '__main__':
    time_a = "10:30"
    time_b = "11:45"
    try:
        result = time_difference(time_a, time_b)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    time_c = "09:00"
    time_d = "08:30"
    try:
        result = time_difference(time_c, time_d)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    time_e = "15:00"
    time_f = "15:00"
    try:
        result = time_difference(time_e, time_f)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")