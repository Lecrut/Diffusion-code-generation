def calculate_time_difference(time_str1: str, time_str2: str) -> int:
    time_format = '%H:%M'
    time1 = datetime.datetime.strptime(time_str1, time_format)
    time2 = datetime.datetime.strptime(time_str2, time_format)
    diff = abs((time2 - time1).seconds) // 60
    return diff

if __name__ == '__main__':
    t1 = "09:30"
    t2 = "14:45"
    result = calculate_time_difference(t1, t2)
    print(result)