from datetime import datetime

def calculate_time_difference(time1_str, time2_str):
    format_str = "%H:%M"
    time1 = datetime.strptime(time1_str, format_str)
    time2 = datetime.strptime(time2_str, format_str)
    return abs((time2 - time1).seconds)

if __name__ == '__main__':
    time1 = "08:00"
    time2 = "16:45"
    difference = calculate_time_difference(time1, time2)
    print(difference)