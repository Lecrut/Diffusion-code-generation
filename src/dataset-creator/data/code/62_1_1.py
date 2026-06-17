import datetime
def add_months(date: datetime.date, months: int) -> datetime.date:
    year = date.year + (months // 12)
    month = date.month - 1 + ((months % 12))
    if month > 12:
        month -= 12
        year += 1
    elif month < 0:
        month += 12
        year -= 1
    try:
        return datetime.date(year, month, date.day)
    except ValueError:
        last_day = datetime.date(year, month + 1, 1).day - 1
        return datetime.date(year, month, last_day)
if __name__ == '__main__':
    today = datetime.date.today()
    new_date = add_months(today, 3)
    print(new_date.strftime("%Y-%m-%d"))