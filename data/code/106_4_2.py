from datetime import date

def absolute_year_difference(date1: date, date2: date) -> int:
    diff = date2 - date1
    days = abs(diff.days)
    years = days // 365
    return years

if __name__ == '__main__':
    d1 = date(2020, 1, 1)
    d2 = date(2025, 1, 1)
    result = absolute_year_difference(d1, d2)
    print(result)