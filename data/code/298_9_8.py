from datetime import datetime, timedelta

def parse_time(time_str: str) -> datetime:
    format_str = "%H:%M"
    return datetime.strptime(time_str, format_str)

def time_difference_minutes(time1: str, time2: str) -> int:
    start_time = parse_time(time1)
    end_time = parse_time(time2)
    
    if start_time > end_time:
        end_time += timedelta(days=1)
    
    return (end_time - start_time).seconds // 60

if __name__ == '__main__':
    result = time_difference_minutes('09:45', '23:15')
    print(result)