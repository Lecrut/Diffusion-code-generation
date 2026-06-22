from datetime import date

YEARS_TO_DAYS = 365.2425

def calculate_absolute_year_gap(start_date: date, end_date: date) -> int:
    delta = end_date - start_date
    total_days = abs(delta.days)
    years_count = total_days / YEARS_TO_DAYS
    return int(years_count)

if __name__ == '__main__':
    initial = date(2015, 6, 15)
    final = date(2023, 6, 15)
    gap = calculate_absolute_year_gap(initial, final)
    print(gap)