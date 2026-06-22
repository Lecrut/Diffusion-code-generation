from datetime import datetime

def time_diff_ms(time_str1: str, time_str2: str) -> int:
    time_format = "%H:%M:%S"
    dt1 = datetime.strptime(time_str1, time_format)
    dt2 = datetime.strptime(time_str2, time_format)
    diff = abs(dt2 - dt1)
    total_seconds = int(diff.total_seconds())
    milliseconds = int(diff.microseconds / 1000)
    return total_seconds * 1000 + milliseconds

if __name__ == '__main__':
    sample_time1 = "14:35:20"
    sample_time2 = "15:47:59"
    print(time_diff_ms(sample_time1, sample_time2))