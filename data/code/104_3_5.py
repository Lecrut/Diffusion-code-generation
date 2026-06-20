from datetime import date

DAYS_PER_YEAR = 365
DAYS_PER_MONTH = 30

def days_between_dates(date1: date, date2: date) -> int:
    year_diff = abs(date2.year - date1.year)
    month_diff = abs(date2.month - date1.month)
    day_diff = abs(date2.day - date1.day)

    total_days = (year_diff * DAYS_PER_YEAR) + (month_diff * DAYS_PER_MONTH) + day_diff
    return total_days

if __name__ == '__main__':
    sample_date1 = date(2023, 1, 1)
    sample_date2 = date(2023, 1, 15)
    print(days_between_dates(sample_date1, sample_date2))