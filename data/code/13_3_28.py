from datetime import time, timedelta

def time_difference_in_seconds(time_str1, time_str2):
    format_str = '%H:%M:%S'
    t1 = time.fromisoformat(time_str1)
    t2 = time.fromisoformat(time_str2)
    diff = datetime.combine(date.min, t2) - datetime.combine(date.min, t1)
    return abs(int(diff.total_seconds()))
if __name__ == '__main__':
    sample_time1 = '14:30:00'
    sample_time2 = '09:45:00'
    result = time_difference_in_seconds(sample_time1, sample_time2)
    print(result)