from datetime import date

def get_precise_years(start_date: date, end_date: date) -> int:
    year_diff = end_date.year - start_date.year
    month_day_end = (end_date.month, end_date.day)
    month_day_start = (start_date.month, start_date.day)
    if month_day_end < month_day_start:
        year_diff -= 1
    return year_diff

if __name__ == '__main__':
    base_date = date(1995, 8, 20)
    target_date = date(2024, 2, 10)
    calculated_years = get_precise_years(base_date, target_date)
    print(calculated_years)