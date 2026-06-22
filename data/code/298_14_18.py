from datetime import datetime

def parse_time(time_str: str) -> datetime:
    time_format = '%H:%M:%S'
    try:
        return datetime.strptime(time_str, time_format)
    except ValueError:
        raise ValueError('Invalid time format')

def time_diff_in_ms(time_str1: str, time_str2: str) -> int:
    dt1 = parse_time(time_str1)
    dt2 = parse_time(time_str2)
    diff = abs(dt2 - dt1)
    return int(diff.total_seconds() * 1000)
if __name__ == '__main__':
    sample_time1 = '14:30:00'
    sample_time2 = '15:45:30'
    print(time_diff_in_ms(sample_time1, sample_time2))