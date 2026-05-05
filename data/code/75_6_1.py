import datetime
def date_difference_days(date1: datetime.date, date2: datetime.date) -> int:
    return abs((date1 - date2).days)
if __name__ == '__main__':
    d1 = datetime.date(2023, 1, 1)
    d2 = datetime.date(2023, 1, 10)
    result = date_difference_days(d1, d2)
    print(result)
    d3 = datetime.date(2024, 5, 15)
    d4 = datetime.date(2024, 3, 1)
    result2 = date_difference_days(d3, d4)
    print(result2)