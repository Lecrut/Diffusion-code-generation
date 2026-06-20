from datetime import datetime

def calculate_elapsed_hours(time_str1, time_str2):
    try:
        format = "%H:%M:%S"
        time1 = datetime.strptime(time_str1, format)
        time2 = datetime.strptime(time_str2, format)
        diff = abs((time2 - time1).total_seconds())
        return diff / 3600
    except ValueError:
        return "Invalid time format"

if __name__ == '__main__':
    print(calculate_elapsed_hours('12:00:00', '14:30:00'))