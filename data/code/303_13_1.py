import datetime
def time_difference_seconds(time_str1: str, time_str2: str) -> int:
    dt1 = datetime.datetime.fromisoformat(time_str1)
    dt2 = datetime.datetime.fromisoformat(time_str2)
    duration = abs(dt1 - dt2)
    return int(duration.total_seconds())
if __name__ == '__main__':
    time1 = "2023-10-27T10:00:00"
    time2 = "2023-10-27T10:05:30"
    result = time_difference_seconds(time1, time2)
    print(result)