from datetime import datetime

def calculate_elapsed_hours(time_str1, time_str2):
    try:
        format = "%H:%M:%S"
        time1 = datetime.strptime(time_str1, format)
        time2 = datetime.strptime(time_str2, format)
        diff = time2 - time1
        return abs(diff.total_seconds() / 3600.0)
    except ValueError:
        return None

if __name__ == '__main__':
    print(calculate_elapsed_hours('14:30:00', '18:45:00'))
    print(calculate_elapsed_hours('23:59:59', '00:00:01'))
    print(calculate_elapsed_hours('12:34:56', 'invalid_time'))