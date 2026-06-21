import calendar
from datetime import datetime

DAY_CLASSES = {
    calendar.MONDAY: 'weekday',
    calendar.TUESDAY: 'weekday',
    calendar.WEDNESDAY: 'weekday',
    calendar.THURSDAY: 'weekday',
    calendar.FRIDAY: 'weekday',
    calendar.SATURDAY: 'weekend',
    calendar.SUNDAY: 'weekend',
}

def is_weekday(dt: datetime) -> bool:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    day_code = calendar.weekday(dt.year, dt.month, dt.day)
    classification = DAY_CLASSES.get(day_code, 'unknown')
    return classification == 'weekday'

if __name__ == '__main__':
    test_date = datetime(2024, 2, 14)
    result = is_weekday(test_date)
    print(result)
    
    test_date = datetime(2024, 2, 17)
    result = is_weekday(test_date)
    print(result)