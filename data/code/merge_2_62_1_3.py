import datetime
def add_months(date: datetime.date, months: int) -> datetime.date:
    year = date.year + (months // 12)
    month = date.month - 1 + ((months % 12))
    day = min(date.day, [31 if m in {1, 3, 5, 7, 8, 10, 12} else 30 for m in range(1, 13)][month])
    return datetime.date(year, month + 1, day)
if __name__ == '__main__':
    today = datetime.date.today()
    result = add_months(today, 5)
    print(result)