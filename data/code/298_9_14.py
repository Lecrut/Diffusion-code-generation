from datetime import datetime, timedelta

MINUTES_IN_DAY = 24 * 60

def time_difference_minutes(time1: str, time2: str) -> int:
    format_str = "%H:%M"
    start_time = datetime.strptime(time1, format_str)
    end_time = datetime.strptime(time2, format_str)
    
    if end_time < start_time:
        end_time += timedelta(days=1)
    
    difference = (end_time - start_time).seconds // 60
    return difference

if __name__ == '__main__':
    time_diff = time_difference_minutes('09:45', '23:15')
    print(time_diff)