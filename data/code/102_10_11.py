import calendar
from datetime import datetime

DAY_CATEGORIES = {
    calendar.MONDAY: "weekday",
    calendar.TUESDAY: "weekday",
    calendar.WEDNESDAY: "weekday",
    calendar.THURSDAY: "weekday",
    calendar.FRIDAY: "weekday",
    calendar.SATURDAY: "weekend",
    calendar.SUNDAY: "weekend",
}

def is_weekday(dt: datetime) -> bool:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    day_code = calendar.weekday(dt.year, dt.month, dt.day)
    category = DAY_CATEGORIES[day_code]
    return category == "weekday"

if __name__ == '__main__':
    test_date = datetime(2024, 7, 15)
    print(is_weekday(test_date))
    test_weekend = datetime(2024, 7, 20)
    print(is_weekday(test_weekend))