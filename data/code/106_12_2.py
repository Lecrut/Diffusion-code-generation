from datetime import date

def years_between_dates(date1: date, date2: date) -> int:
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    print(years_between_dates(date(2020, 1, 1), date(2023, 4, 1)))