from datetime import datetime

def calculate_time_difference(time1_str, time2_str):
    time_format = "%H:%M"
    time1 = datetime.strptime(time1_str, time_format)
    time2 = datetime.strptime(time2_str, time_format)
    if time1 > time2:
        time2 += datetime.strptime("24:00", time_format) - datetime.strptime("00:00", time_format)
    return (time2 - time1).seconds // 60

if __name__ == '__main__':
    diff = calculate_time_difference('23:59', '00:01')
    print(diff)