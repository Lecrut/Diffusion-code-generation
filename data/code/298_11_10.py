from datetime import datetime

def time_difference_seconds(time1_str, time2_str):
    format_str = "%H:%M"
    time1 = datetime.strptime(time1_str, format_str)
    time2 = datetime.strptime(time2_str, format_str)
    return abs((time2 - time1).seconds)

if __name__ == '__main__':
    print(time_difference_seconds('14:30', '16:45'))