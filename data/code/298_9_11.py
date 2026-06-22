from datetime import datetime

def time_difference_minutes(time1: str, time2: str) -> int:
    format_str = "%H:%M"
    
    try:
        start_time = datetime.strptime(time1, format_str)
        end_time = datetime.strptime(time2, format_str)
    except ValueError:
        raise ValueError("Invalid time format. Please use HH:MM")
    
    if start_time > end_time:
        end_time += timedelta(days=1)
    
    return (end_time - start_time).seconds // 60

if __name__ == '__main__':
    print(time_difference_minutes('09:45', '23:15'))