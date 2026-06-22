from datetime import datetime

def time_difference_in_hours(time1: str, time2: str) -> float:
    format_str = "%H:%M"
    start_time = datetime.strptime(time1, format_str)
    end_time = datetime.strptime(time2, format_str)
    
    if end_time < start_time:
        end_time += timedelta(days=1)
    
    return (end_time - start_time).total_seconds() / 3600

if __name__ == '__main__':
    print(time_difference_in_hours('12:00', '19:30'))
    print(time_difference_in_hours('19:30', '12:00'))