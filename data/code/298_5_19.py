from datetime import datetime

def time_difference_in_hours(time1, time2):
    format_str = "%H:%M"
    tdelta = datetime.strptime(time2, format_str) - datetime.strptime(time1, format_str)
    return abs(tdelta.total_seconds() / 3600)

if __name__ == '__main__':
    print(time_difference_in_hours('12:00', '19:30'))
    print(time_difference_in_hours('19:30', '12:00'))