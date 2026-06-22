from datetime import datetime, timedelta

def time_difference_minutes(time1: str, time2: str) -> int:
    format_str = "%H:%M"
    start_time = datetime.strptime(time1, format_str)
    end_time = datetime.strptime(time2, format_str)
    
    if end_time < start_time:
        end_time += timedelta(days=1)
    
    return (end_time - start_time).seconds // 60

if __name__ == '__main__':
    print(time_difference_minutes('09:45', '23:15'))