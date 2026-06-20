from datetime import date
DAYS_PER_YEAR = 365

def calculate_year_difference(date1: date, date2: date) -> int:
    if date1 > date2:
        date1, date2 = (date2, date1)
    year_diff = date2.year - date1.year
    leap_years_count = sum(((date1.year + i) % 4 == 0 for i in range(year_diff)))
    if (date1.year % 4 == 0 or date1.year % 400 == 0) and date2.year % 4 != 0:
        leap_years_count -= 1
    days_diff = abs((date2 - date1).days)
    total_days_diff = days_diff + leap_years_count * DAYS_PER_YEAR
    year_diff += total_days_diff // DAYS_PER_YEAR
    return year_diff
if __name__ == '__main__':
    sample_date1 = date(1980, 7, 4)
    sample_date2 = date(2023, 10, 11)
    print(calculate_year_difference(sample_date1, sample_date2))