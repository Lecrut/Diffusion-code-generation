from datetime import datetime

def time_difference(time1, time2):
    format_str = "%H:%M"
    tdelta = datetime.strptime(time2, format_str) - datetime.strptime(time1, format_str)
    return tdelta.total_seconds()

if __name__ == '__main__':
    result = time_difference('14:30', '16:45')
    print(result)