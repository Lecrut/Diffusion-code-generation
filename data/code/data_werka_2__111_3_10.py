from datetime import date, timedelta
import calendar

def subtract_months(d: date, months: int) -> date:
    month = d.month - 1 - (months % 12)
    year = d.year - months // 12 - (1 if month < 0 else 0)
    month = month % 12 + 1
    day = min(d.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)

if __name__ == '__main__':
    original_date = date(2023, 10, 15)
    result = subtract_months(original_date, 3)
    print(result)