def convert_duration(time_str):
    h, m, s = map(int, time_str.split(':'))
    days = 0
    hours = h
    minutes = m
    seconds = s
    if hours >= 24:
        days = hours // 24
        hours = hours % 24
    if days > 0:
        return f"{days} Days, {hours} Hours, {minutes} Minutes, {seconds} Seconds"
    else:
        return f"{hours} Hours, {minutes} Minutes, {seconds} Seconds"
if __name__ == '__main__':
    test_time1 = "25:30:15"
    test_time2 = "10:15:45"
    test_time3 = "48:72:10"
    test_time4 = "0:0:0"
    print(f"Input: {test_time1}, Output: {convert_duration(test_time1)}")
    print(f"Input: {test_time2}, Output: {convert_duration(test_time2)}")
    print(f"Input: {test_time3}, Output: {convert_duration(test_time3)}")
    print(f"Input: {test_time4}, Output: {convert_duration(test_time4)}")