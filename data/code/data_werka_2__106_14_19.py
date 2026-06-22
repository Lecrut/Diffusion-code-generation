from datetime import datetime

def year_difference(date1: datetime, date2: datetime) -> int:
    diff = abs(date1 - date2)
    days = diff.days
    years = days // 365
    return years

if __name__ == '__main__':
    d1 = datetime(2023, 10, 1)
    d2 = datetime(2020, 10, 1)
    result = year_difference(d1, d2)
    print(result)