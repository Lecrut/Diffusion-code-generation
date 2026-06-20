import datetime

def days_between(date1: datetime.date, date2: datetime.date) -> int:
    if date1 > date2:
        date1, date2 = date2, date1
    return (date2 - date1).days

if __name__ == '__main__':
    date_a = datetime.date(2023, 1, 1)
    date_b = datetime.date(2023, 1, 10)
    result1 = days_between(date_a, date_b)
    print(result1)