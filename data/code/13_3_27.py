from datetime import datetime

def time_difference_in_seconds(time1, time2):
    format_str = "%H:%M:%S"
    t1 = datetime.strptime(time1, format_str)
    t2 = datetime.strptime(time2, format_str)
    delta = t2 - t1
    return abs(delta.total_seconds())

if __name__ == '__main__':
    sample_time1 = "14:30:00"
    sample_time2 = "15:45:00"
    print(time_difference_in_seconds(sample_time1, sample_time2))