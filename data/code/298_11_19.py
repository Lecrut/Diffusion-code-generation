import datetime

def calculate_time_difference(time1_str, time2_str):
    time_format = "%H:%M"
    time1 = datetime.datetime.strptime(time1_str, time_format)
    time2 = datetime.datetime.strptime(time2_str, time_format)
    time_difference = abs((time2 - time1).seconds)
    return time_difference

if __name__ == '__main__':
    sample_time1 = '14:30'
    sample_time2 = '16:45'
    result = calculate_time_difference(sample_time1, sample_time2)
    print(result)