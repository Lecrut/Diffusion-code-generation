from datetime import datetime

def calculate_elapsed_hours(time_str1, time_str2):
    try:
        time_format = '%H:%M:%S'
        time1 = datetime.strptime(time_str1, time_format)
        time2 = datetime.strptime(time_str2, time_format)
        delta = abs((time2 - time1).total_seconds())
        return delta / 3600
    except ValueError:
        return 'Invalid time format'
if __name__ == '__main__':
    print(calculate_elapsed_hours('12:00:00', '14:30:00'))
    print(calculate_elapsed_hours('23:59:59', '00:00:01'))
    print(calculate_elapsed_hours('08:00:00', '07:59:59'))
    print(calculate_elapsed_hours('24:00:00', '00:00:00'))