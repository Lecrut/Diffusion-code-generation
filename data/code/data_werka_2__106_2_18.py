from datetime import datetime

def compute_year_delta(reference: datetime, comparison: datetime) -> int:
    full_years = comparison.year - reference.year
    reference_moments = datetime(reference.year, reference.month, reference.day)
    comparison_moments = datetime(comparison.year, comparison.month, comparison.day)
    elapsed_days = (comparison_moments - reference_moments).days
    leap_adjustment = 0
    current_year = reference.year
    while current_year < comparison.year:
        if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
            leap_adjustment += 1
        current_year += 1
    total_approx_days = full_years * 365 + leap_adjustment
    if elapsed_days < total_approx_days:
        full_years -= 1
    return full_years

if __name__ == '__main__':
    start_date = datetime(1980, 11, 5)
    end_date = datetime(2021, 11, 4)
    delta = compute_year_delta(start_date, end_date)
    print(delta)