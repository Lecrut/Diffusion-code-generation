from datetime import date

def calculate_full_years(start_date: date, end_date: date) -> int:
    if start_date > end_date:
        raise ValueError("Start date must be before end date.")
    
    year_diff = end_date.year - start_date.year
    month_day_diff = (end_date.month, end_date.day) < (start_date.month, start_date.day)
    
    return year_diff - month_day_diff

if __name__ == '__main__':
    sample_start = date(2015, 12, 25)
    sample_end = date(2024, 1, 1)
    print(calculate_full_years(sample_start, sample_end))