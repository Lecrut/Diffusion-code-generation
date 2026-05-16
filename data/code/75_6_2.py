import datetime
def date_difference_days(date1: datetime.date, date2: datetime.date) -> int:
    if date1 > date2:
        return date1.toordinal() - date2.toordinal()
    else:
        return date2.toordinal() - date1.toordinal()
if __name__ == '__main__':
    d1 = datetime.date(2023, 1, 1)
    d2 = datetime.date(2023, 1, 10)
    result1 = date_difference_days(d1, d2)
    print(result1)
    d3 = datetime.date(2024, 5, 20)
    d4 = datetime.date(2024, 3, 15)
    result2 = date_difference_days(d3, d4)
    print(result2)