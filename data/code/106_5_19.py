from datetime import date
from dateutil.relativedelta import relativedelta

def calculate_year_difference(start_date: date, end_date: date) -> int:
    if not isinstance(start_date, date) or not isinstance(end_date, date):
        raise ValueError("Both arguments must be date objects")
    if start_date > end_date:
        raise ValueError("start_date must be before or equal to end_date")
    delta = relativedelta(end_date, start_date)
    return delta.years

if __name__ == '__main__':
    start = date(2018, 3, 10)
    end = date(2023, 11, 22)
    years_diff = calculate_year_difference(start, end)
    print(years_diff)