from datetime import date

def years_between_dates(date1: date, date2: date) -> int:
    delta = abs((date2 - date1).days)
    return delta // 365 + (delta % 365 > 0)

if __name__ == '__main__':
    d1 = date(2010, 1, 1)
    d2 = date(2023, 4, 15)
    print(years_between_dates(d1, d2))