from datetime import datetime

def calculate_elapsed_hours(time_str1, time_str2):
    try:
        time_format = "%H:%M:%S"
        start_time = datetime.strptime(time_str1, time_format)
        end_time = datetime.strptime(time_str2, time_format)
        elapsed_time = end_time - start_time
        return abs(elapsed_time.total_seconds() / 3600.0)
    except ValueError:
        return "Invalid time format"

if __name__ == '__main__':
    print(calculate_elapsed_hours("14:30:00", "17:45:00"))
    print(calculate_elapsed_hours("23:59:59", "00:00:01"))
    print(calculate_elapsed_hours("08:00:00", "07:59:59"))
    print(calculate_elapsed_hours("24:00:00", "00:00:00"))