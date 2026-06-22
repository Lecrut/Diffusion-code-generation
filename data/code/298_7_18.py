from datetime import datetime

def time_difference_in_seconds(time_str1, time_str2):
    time_format = "%H:%M"
    time1 = datetime.strptime(time_str1, time_format)
    time2 = datetime.strptime(time_str2, time_format)
    duration = (time2 - time1).seconds
    return duration

if __name__ == '__main__':
    sample_time1 = "10:45"
    sample_time2 = "13:20"
    result = time_difference_in_seconds(sample_time1, sample_time2)
    print(f"Time difference between {sample_time1} and {sample_time2}: {result} seconds")