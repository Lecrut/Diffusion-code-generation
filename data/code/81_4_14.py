from datetime import datetime

def time_difference_hours(time_str1: str, time_str2: str) -> float:
    time_format = '%H:%M:%S'
    start_time = datetime.strptime(time_str1, time_format)
    end_time = datetime.strptime(time_str2, time_format)
    duration = abs(end_time - start_time)
    return duration.total_seconds() / 3600.0

if __name__ == '__main__':
    time1 = '09:00:00'
    time2 = '17:30:00'
    result = time_difference_hours(time1, time2)
    print(result)