from datetime import date

def years_between_dates(date1: date, date2: date) -> int:
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    d1 = date(2010, 1, 1)
    d2 = date(2023, 4, 15)
    print(years_between_dates(d1, d2))