from datetime import date

def years_difference(date1: date, date2: date) -> int:
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    print(years_difference(date(2020, 1, 1), date(2023, 4, 1)))
    print(years_difference(date(2019, 12, 31), date(2020, 1, 1)))