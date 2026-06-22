from datetime import date
from calendar import isleap

def calculate_year_difference(d1: date, d2: date) -> int:
    if d1 > d2:
        d1, d2 = d2, d1
    years = d2.year - d1.year
    if d1.month < d2.month:
        return years
    if d1.month > d2.month:
        return years - 1
    if d1.day > d2.day:
        return years - 1
    return years

if __name__ == '__main__':
    start_date = date(2019, 12, 31)
    end_date = date(2023, 1, 1)
    diff = calculate_year_difference(start_date, end_date)
    print(diff)