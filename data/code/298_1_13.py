from datetime import datetime

def time_difference_seconds(time1, time2):
    format_str = "%H:%M"
    t1 = datetime.strptime(time1, format_str)
    t2 = datetime.strptime(time2, format_str)
    delta = t2 - t1
    return delta.total_seconds()

if __name__ == '__main__':
    print(int(time_difference_seconds('14:30', '16:45')))