from datetime import datetime

def validate_time_format(time_str):
    try:
        datetime.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False

def time_difference_seconds(time1, time2):
    if not (validate_time_format(time1) and validate_time_format(time2)):
        raise ValueError("Invalid time format. Please use 'HH:MM'.")

    format_str = "%H:%M"
    tdelta = datetime.strptime(time2, format_str) - datetime.strptime(time1, format_str)
    return abs(tdelta.total_seconds())

if __name__ == '__main__':
    print(int(time_difference_seconds('14:30', '16:45')))