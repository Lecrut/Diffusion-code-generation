import datetime
def add_months(date: datetime.date, months: int) -> datetime.date:
    year = date.year + (months // 12)
    month = date.month + (months % 12) - 1
    if month > 11:
        raise ValueError("Invalid input for adding months")
    day = min(date.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month + 1, day)
import calendar
if __name__ == '__main__':
    sample_date = datetime.date(2023, 5, 31)
    months_to_add = 7
    result_date = add_months(sample_date, months_to_add)
    print(f"Original Date: {sample_date}")
    print(f"Menthods to Add: {months_to_add}")
    print(f"Resulting Date: {result_date}")