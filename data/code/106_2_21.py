from datetime import datetime

MONTHS_IN_YEAR = 12
DATE_COMPARISON_THRESHOLD = 0

def calculate_full_years(start_dt: datetime, end_dt: datetime) -> int:
    if start_dt > end_dt:
        raise ValueError("Start date must be before or equal to end date")
    
    year_diff = end_dt.year - start_dt.year
    
    if year_diff == 0:
        return DATE_COMPARISON_THRESHOLD
    
    start_reference = datetime(start_dt.year + year_diff, start_dt.month, start_dt.day)
    
    if end_dt < start_reference:
        return year_diff - 1
    
    return year_diff

if __name__ == '__main__':
    date_a = datetime(2010, 3, 15)
    date_b = datetime(2020, 3, 14)
    diff = calculate_full_years(date_a, date_b)
    print(diff)