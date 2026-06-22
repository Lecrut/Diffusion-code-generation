from datetime import date, timedelta

def compute_days_in_year(year):
    if year < 1:
        raise ValueError("Year must be positive")
    start = date(year, 1, 1)
    next_year_start = date(year + 1, 1, 1)
    delta = next_year_start - start
    return delta.days

if __name__ == '__main__':
    target_year = 2023
    days = compute_days_in_year(target_year)
    print(days)