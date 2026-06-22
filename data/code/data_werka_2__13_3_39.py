from datetime import datetime

def time_difference_in_seconds(time_str1, time_str2):
    try:
        time_format = '%H:%M:%S'
        time1 = datetime.strptime(time_str1, time_format)
        time2 = datetime.strptime(time_str2, time_format)
        delta = time2 - time1
        return abs(delta.total_seconds())
    except ValueError as e:
        raise ValueError("Invalid time format. Please use 'HH:MM:SS'.")
if __name__ == '__main__':
    sample_time1 = '14:30:00'
    sample_time2 = '15:45:30'
    difference_seconds = time_difference_in_seconds(sample_time1, sample_time2)
    print(difference_seconds)