from datetime import datetime

def year_difference(date1: datetime, date2: datetime) -> int:
    delta = date2 - date1
    days = delta.days
    years = days // 365
    return years

if __name__ == '__main__':
    d1 = datetime(2020, 1, 1)
    d2 = datetime(2023, 6, 15)
    result = year_difference(d1, d2)
    print(result)