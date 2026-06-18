import datetime
def add_months(date: datetime.date, months: int) -> datetime.date:
    year = date.year + (months // 12)
    month = date.month - 1 + ((months % 12))
    if month > 0 and month <= 12:
        return datetime.date(year, month, date.day)
    else:
        new_month = month + 13
        year -= 1
        return add_months(datetime.date(year, new_month - 12, date.day), months % 12)
if __name__ == '__main__':
    today = datetime.date.today()
    result_date = add_months(today, 5)
    print(result_date.strftime('%Y-%m-%d'))