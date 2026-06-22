import datetime

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def time_to_seconds(time_str: str) -> int:
    hours, minutes, seconds = map(int, time_str.split(':'))
    return (hours * SECONDS_PER_HOUR) + (minutes * SECONDS_PER_MINUTE) + seconds

def time_diff_in_milliseconds(time_str1: str, time_str2: str) -> int:
    time1_seconds = time_to_seconds(time_str1)
    time2_seconds = time_to_seconds(time_str2)
    difference_seconds = abs(time1_seconds - time2_seconds)
    return difference_seconds * 1000

if __name__ == '__main__':
    print(time_diff_in_milliseconds("14:30:00", "15:45:00"))
    print(time_diff_in_milliseconds("09:00:00", "22:00:00"))