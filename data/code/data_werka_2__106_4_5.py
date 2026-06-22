from datetime import date

def absolute_year_difference(date1: date, date2: date) -> int:
    delta = date1 - date2
    days = abs(delta.days)
    years = days // 365
    return years

if __name__ == '__main__':
    d1 = date(2023, 10, 15)
    d2 = date(2020, 10, 15)
    result = absolute_year_difference(d1, d2)
    print(result)