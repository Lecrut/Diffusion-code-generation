import datetime

def same_week(date1: datetime.date, date2: datetime.date) -> bool:
    iso1 = date1.isocalendar()
    iso2 = date2.isocalendar()
    return iso1[:2] == iso2[:2]

if __name__ == '__main__':
    d1 = datetime.date(2023, 1, 1)
    d2 = datetime.date(2023, 1, 7)
    d3 = datetime.date(2023, 1, 8)
    print(same_week(d1, d2))
    print(same_week(d1, d3))