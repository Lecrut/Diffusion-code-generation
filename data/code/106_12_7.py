from datetime import date

def years_between_dates(date1: date, date2: date) -> int:
    delta = abs(date2 - date1)
    days_in_year = 365.25
    return int(delta.days / days_in_year)
if __name__ == '__main__':
    d1 = date(1980, 7, 4)
    d2 = date(2023, 10, 25)
    print(years_between_dates(d1, d2))