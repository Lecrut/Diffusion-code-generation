import datetime
def time_difference(time_str1, time_str2):
    time_format = "%H:%M"
    try:
        time1 = datetime.datetime.strptime(time_str1, time_format)
        time2 = datetime.datetime.strptime(time_str2, time_format)
    except ValueError:
        raise ValueError("Invalid time format. Please use 'HH:MM'.")
    if time2 > time1:
        diff = (time2 - time1).total_seconds() / 60
        return int(diff)
    else:
        raise ValueError("The second time is not chronologically after the first time.")
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
    time_g = "23:59"
    time_h = "00:01"
    try:
        result = time_difference(time_g, time_h)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")