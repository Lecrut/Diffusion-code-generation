from datetime import datetime

def time_difference_in_seconds(time_str1, time_str2):
    format_str = "%H:%M:%S"
    time_obj1 = datetime.strptime(time_str1, format_str)
    time_obj2 = datetime.strptime(time_str2, format_str)
    difference = abs((time_obj2 - time_obj1).total_seconds())
    return difference

if __name__ == '__main__':
    sample_time1 = "14:30:00"
    sample_time2 = "09:45:00"
    print(time_difference_in_seconds(sample_time1, sample_time2))