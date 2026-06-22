from datetime import datetime

def time_difference_in_seconds(time_str1, time_str2):
    TIME_FORMAT = '%H:%M:%S'
    start_time = datetime.strptime(time_str1, TIME_FORMAT)
    end_time = datetime.strptime(time_str2, TIME_FORMAT)
    time_delta = end_time - start_time
    return abs(int(time_delta.total_seconds()))
if __name__ == '__main__':
    sample_start_time = '08:15:30'
    sample_end_time = '17:45:45'
    difference_in_seconds = time_difference_in_seconds(sample_start_time, sample_end_time)
    print(difference_in_seconds)