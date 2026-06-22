from datetime import datetime

def time_difference_seconds(time_str1, time_str2):
    format_str = "%H:%M"
    time_obj1 = datetime.strptime(time_str1, format_str)
    time_obj2 = datetime.strptime(time_str2, format_str)
    return abs((time_obj2 - time_obj1).seconds)

if __name__ == '__main__':
    print(time_difference_seconds('14:30', '16:45'))