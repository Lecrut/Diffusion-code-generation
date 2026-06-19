from datetime import datetime

def time_difference_in_seconds(time_str1, time_str2):
    format_str = "%H:%M:%S"
    time1 = datetime.strptime(time_str1, format_str)
    time2 = datetime.strptime(time_str2, format_str)
    delta = time2 - time1
    return abs(delta.total_seconds())

if __name__ == '__main__':
    sample_time1 = "10:30:45"
    sample_time2 = "15:45:30"
    print(time_difference_in_seconds(sample_time1, sample_time2))