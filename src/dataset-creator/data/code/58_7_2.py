from datetime import date
def calculate_days_between(date1: date, date2: date) -> dict:
    total_calendar_days = (date2 - date1).days
    business_days = 0
    current_date = date1 + timedelta(days=1) if date1 < date2 else date1
    end_date = date2 + timedelta(days=1) if date2 > date1 else date2
    while current_date != end_date:
        weekday = current_date.weekday()
        if weekday not in (5, 6):
            business_days += 1
        current_date += timedelta(days=1)
    return {
        "total_calendar_days": total_calendar_days,
        "business_days": business_days
    }
from datetime import date, timedelta
if __name__ == '__main__':
    start = date(2023, 6, 5)
    end = date(2023, 7, 1)
    result = calculate_days_between(start, end)
    print(result)