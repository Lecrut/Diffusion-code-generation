from datetime import datetime

def time_difference_in_seconds(time1, time2):
    format_str = "%H:%M"
    datetime_obj1 = datetime.strptime(time1, format_str)
    datetime_obj2 = datetime.strptime(time2, format_str)
    delta = datetime_obj2 - datetime_obj1
    return delta.total_seconds()

if __name__ == '__main__':
    print(int(time_difference_in_seconds('14:30', '16:45')))