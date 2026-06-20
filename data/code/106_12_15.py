from datetime import date

def years_between(date1: date, date2: date) -> int:
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    date1 = date(1990, 5, 15)
    date2 = date(2023, 8, 24)
    print(years_between(date1, date2))