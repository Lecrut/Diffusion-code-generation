import datetime

def calculate_time_difference(start_time_str, end_time_str):
    time_format = "%H:%M:%S"
    try:
        start_time = datetime.datetime.strptime(start_time_str, time_format)
        end_time = datetime.datetime.strptime(end_time_str, time_format)
    except ValueError:
        raise ValueError("Invalid time format. Please use HH:MM:SS.")
    
    if end_time < start_time:
        end_time += datetime.timedelta(days=1)
    
    elapsed_time = end_time - start_time
    total_seconds = elapsed_time.total_seconds()
    total_hours = total_seconds / 3600.0
    return total_hours

if __name__ == '__main__':
    start_time_str = "09:00:00"
    end_time_str = "17:30:00"
    difference = calculate_time_difference(start_time_str, end_time_str)
    print(f"{difference}")