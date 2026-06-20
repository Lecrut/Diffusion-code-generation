from datetime import datetime

def calculate_duration(date1: datetime, date2: datetime) -> timedelta:
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError("Both inputs must be datetime objects")
    
    duration = abs(date2 - date1)
    return duration

if __name__ == '__main__':
    date1 = datetime(2023, 10, 1, 12, 0, 0)
    date2 = datetime(2023, 10, 1, 14, 30, 0)
    print(calculate_duration(date1, date2))