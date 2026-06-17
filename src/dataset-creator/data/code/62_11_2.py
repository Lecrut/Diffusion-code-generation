import datetime
def add_months(date_str: str, n: int) -> str:
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    year = date_obj.year + (n // 12)
    month = ((date_obj.month - 1 + n % 12) % 12) + 1
    try:
        new_date = date_obj.replace(year=year, month=month)
    except ValueError:
        last_day_of_month = datetime.datetime(year, month, 30).replace(day=datetime.date(year, month, 1).day if len(str(datetime.date(year, month, 1))) == 2 else 31)
        try:
            new_date = date_obj.replace(year=year, month=month + (n % 12))
        except ValueError:
            last_day_of_month = datetime.datetime(year, month - 1, 0).replace(day=datetime.date(year, month - 1, 1).day if len(str(datetime.date(year, month - 1, 1))) == 2 else 31)
    return new_date.strftime("%Y-%m-%d")
if __name__ == '__main__':
    print(add_months("2024-02-28", 5))