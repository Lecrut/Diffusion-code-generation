from datetime import datetime

def calculate_time_difference(start: datetime, end: datetime) -> dict:
    delta = end - start
    total_seconds = int(delta.total_seconds())
    
    if total_seconds < 0:
        total_seconds = abs(total_seconds)
        sign = -1
    else:
        sign = 1
        
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    
    return {
        "hours": sign * hours,
        "minutes": minutes,
        "seconds": seconds
    }

if __name__ == '__main__':
    start_time = datetime(2023, 10, 1, 10, 0, 0)
    end_time = datetime(2023, 10, 1, 12, 30, 45)
    
    result = calculate_time_difference(start_time, end_time)
    print(result)