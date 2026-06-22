from datetime import date
from math import floor

def get_exact_year_difference(start_date: date, end_date: date) -> int:
    delta_days = (end_date - start_date).days
    if start_date <= end_date:
        years_estimate = floor(delta_days / 365.25)
        temp_date = date(start_date.year + years_estimate, start_date.month, start_date.day)
        if temp_date > end_date:
            return years_estimate - 1
        return years_estimate
    negative_days = -delta_days
    years_estimate = floor(negative_days / 365.25)
    temp_date = date(end_date.year + years_estimate, end_date.month, end_date.day)
    if temp_date < end_date:
        return -(years_estimate - 1)
    return -years_estimate

if __name__ == '__main__':
    start = date(1990, 6, 15)
    end = date(2021, 6, 14)
    diff = get_exact_year_difference(start, end)
    print(diff)