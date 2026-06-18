import datetime
def add_months(date: datetime.date, months: int) -> datetime.date:
    year = date.year + (months // 12)
    month = ((date.month - 1 + months) % 12) + 1
    day = min(date.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)
import calendar
if __name__ == '__main__':
    today = datetime.date(2023, 5, 15)
    n_months = 7
    target_date = add_months(today, n_months)
    print(target_date.strftime('%Y-%m-%d'))