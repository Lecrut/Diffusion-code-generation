def convert_duration(time_str):
    h, m, s = map(int, time_str.split(':'))
    days = 0
    hours = h
    minutes = m
    seconds = s
    if hours >= 24:
        days = hours // 24
        hours = hours % 24
    return f"{days} Days, {hours} Hours, {minutes} Minutes, {seconds} Seconds"
if __name__ == '__main__':
    time1 = "25:60:00"
    time2 = "48:15:30"
    time3 = "01:05:00"
    time4 = "86:30:45"
    print(convert_duration(time1))
    print(convert_duration(time2))
    print(convert_duration(time3))
    print(convert_duration(time4))