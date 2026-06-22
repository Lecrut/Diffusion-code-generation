from datetime import date
import calendar

def calculate_year_difference(start_date: date, end_date: date) -> int:
    if not isinstance(start_date, date) or not isinstance(end_date, date):
        raise ValueError("Inputs must be date objects")
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    years = end_date.year - start_date.year
    month_diff = end_date.month - start_date.month
    if month_diff < 0:
        years -= 1
    elif month_diff == 0:
        if end_date.day < start_date.day:
            years -= 1
    return years

if __name__ == '__main__':
    start = date(2010, 6, 15)
    end = date(2023, 6, 14)
    result = calculate_year_difference(start, end)
    print(result)