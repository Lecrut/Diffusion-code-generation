from datetime import datetime

def time_difference_in_seconds(time1_str, time2_str):
    time_format = '%H:%M'
    time1 = datetime.strptime(time1_str, time_format)
    time2 = datetime.strptime(time2_str, time_format)
    difference = abs((time2 - time1).total_seconds())
    return int(difference)

if __name__ == '__main__':
    sample_time1 = '14:30'
    sample_time2 = '16:45'
    result = time_difference_in_seconds(sample_time1, sample_time2)
    print(result)