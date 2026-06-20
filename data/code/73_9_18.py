import datetime

def calculate_time_difference(date1: datetime.datetime, date2: datetime.datetime) -> datetime.timedelta:
    if not isinstance(date1, datetime.datetime) or not isinstance(date2, datetime.datetime):
        raise ValueError("Both inputs must be datetime objects.")
    
    return abs(date1 - date2)

if __name__ == '__main__':
    date1 = datetime.datetime(2023, 1, 15)
    date2 = datetime.datetime(2023, 2, 20)
    result = calculate_time_difference(date1, date2)
    print(f"Date 1: {date1}")
    print(f"Date 2: {date2}")
    print(f"Time Difference: {result}")