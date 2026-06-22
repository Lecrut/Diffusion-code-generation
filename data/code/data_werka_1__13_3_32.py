from datetime import datetime

def time_difference_in_seconds(time1: str, time2: str) -> int:
    format_str = "%H:%M:%S"
    t1 = datetime.strptime(time1, format_str)
    t2 = datetime.strptime(time2, format_str)
    difference = abs((t2 - t1).total_seconds())
    return int(difference)

if __name__ == '__main__':
    time_point1 = "14:30:00"
    time_point2 = "09:15:00"
    print(time_difference_in_seconds(time_point1, time_point2))