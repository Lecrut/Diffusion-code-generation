import datetime

def is_weekday(year: int, month: int, day: int) -> bool:
    if not isinstance(year, int):
        raise ValueError("Year must be an integer")
    if not isinstance(month, int):
        raise ValueError("Month must be an integer")
    if not isinstance(day, int):
        raise ValueError("Day must be an integer")
    
    try:
        date_obj = datetime.date(year, month, day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")
    
    return date_obj.weekday() < 5

if __name__ == '__main__':
    result = is_weekday(2023, 10, 23)
    print(result)
    
    result2 = is_weekday(2023, 10, 21)
    print(result2)