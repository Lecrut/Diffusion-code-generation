import datetime
def add_months(date_str: str, n: int) -> str:
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    year = dt.year + (n // 12)
    month = dt.month - 1 + ((n % 12))
    if month > 12:
        month -= 12
        year += 1
    elif month < 0:
        month += 12
        year -= 1
    day = min(dt.day, datetime.date(year, month + 1, 1).day)
    return dt.replace(year=year, month=month+1, day=day).strftime("%Y-%m-%d")
if __name__ == '__main__':
    print(add_months("2023-05-31", 6))