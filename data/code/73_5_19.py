from datetime import datetime, timedelta

def calculate_time_difference(start: datetime, end: datetime) -> timedelta:
    if not isinstance(start, datetime):
        raise ValueError("start must be a datetime object")
    if not isinstance(end, datetime):
        raise ValueError("end must be a datetime object")
    
    delta = end - start
    
    if delta.days < 0:
        return delta
    if delta.days == 0 and delta.seconds == 0 and delta.microseconds == 0:
        return timedelta(0)
        
    return delta

def get_signed_seconds(delta: timedelta) -> int:
    total_seconds = delta.total_seconds()
    return int(total_seconds)

if __name__ == '__main__':
    start_time = datetime(2023, 12, 25, 10, 0, 0)
    end_time = datetime(2023, 12, 25, 8, 30, 0)
    
    diff = calculate_time_difference(start_time, end_time)
    seconds = get_signed_seconds(diff)
    
    print(diff)
    print(seconds)