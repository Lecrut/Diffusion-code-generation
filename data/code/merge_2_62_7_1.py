import datetime
def add_months(date: datetime.date, months: int) -> datetime.date:
    year = date.year + (months // 12)
    month = ((date.month - 1 + months) % 12) + 1
    day = min(date.day, [31 if m in {1, 3, 5, 7, 8, 10, 12} else (29 if m == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28) for m in range(1, 13)][month - 1])
    return datetime.date(year, month, day)
if __name__ == '__main__':
    today = datetime.date.today()
    n_months = 6
    result_date = add_months(today, n_months)
    print(result_date.strftime('%Y-%m-%d'))