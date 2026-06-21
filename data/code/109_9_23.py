import calendar
from datetime import date

def compute_remaining_days_in_current_month(reference_date: date) -> int:
    year = reference_date.year
    month = reference_date.month
    last_day_of_month = calendar.monthrange(year, month)[1]
    end_date = date(year, month, last_day_of_month)
    remaining = (end_date - reference_date).days
    return remaining

if __name__ == '__main__':
    sample_date = date(2024, 2, 10)
    result = compute_remaining_days_in_current_month(sample_date)
    print(result)