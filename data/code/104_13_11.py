import datetime

def same_week(date1: datetime.date, date2: datetime.date) -> bool:
    iso1 = date1.isocalendar()
    iso2 = date2.isocalendar()
    return iso1[0] == iso2[0] and iso1[1] == iso2[1]

if __name__ == '__main__':
    d1 = datetime.date(2023, 1, 1)
    d2 = datetime.date(2023, 1, 7)
    print(same_week(d1, d2))