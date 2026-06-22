from datetime import datetime

def time_difference_minutes(time1: str, time2: str) -> int:
    format_str = "%H:%M"
    time_obj1 = datetime.strptime(time1, format_str)
    time_obj2 = datetime.strptime(time2, format_str)
    
    if time_obj1 > time_obj2:
        time_obj2 += timedelta(days=1)
    
    return (time_obj2 - time_obj1).total_seconds() / 60

if __name__ == '__main__':
    print(time_difference_minutes('09:45', '23:15'))