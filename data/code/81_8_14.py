from datetime import datetime

def validate_time(time_str):
    try:
        return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S%z")
    except ValueError:
        raise ValueError("Invalid time format. Please use 'YYYY-MM-DD HH:MM:SS+/-HHMM'")

def calculate_elapsed_hours(start_time, end_time):
    if start_time > end_time:
        start_time, end_time = end_time, start_time
    return (end_time - start_time).total_seconds() / 3600

if __name__ == '__main__':
    try:
        start_time_str = "2023-10-01 12:00:00+0000"
        end_time_str = "2023-10-01 14:30:00+0000"
        
        start_time = validate_time(start_time_str)
        end_time = validate_time(end_time_str)
        
        elapsed_hours = calculate_elapsed_hours(start_time, end_time)
        print(f"Elapsed hours: {elapsed_hours:.2f}")
    except ValueError as e:
        print(e)