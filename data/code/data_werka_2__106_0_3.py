from datetime import date
from dateutil.relativedelta import relativedelta

def get_year_diff(d1: date, d2: date) -> int:
    delta = relativedelta(d2, d1)
    return delta.years

if __name__ == '__main__':
    start = date(1995, 5, 15)
    end = date(2024, 8, 20)
    diff = get_year_diff(start, end)
    print(diff)