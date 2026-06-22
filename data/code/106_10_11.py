from datetime import datetime

DIFFERENCE_THRESHOLD_MONTH = 12

def calculate_full_year_difference(start_date: datetime, end_date: datetime) -> int:
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise ValueError("Inputs must be datetime objects")
    
    if start_date == end_date:
        return 0
    
    is_negative = start_date > end_date
    later_date = end_date if not is_negative else start_date
    earlier_date = start_date if not is_negative else end_date
    
    year_diff = later_date.year - earlier_date.year
    
    if year_diff == 0:
        return 0
    
    comparison_date = datetime(
        year=earlier_date.year + year_diff,
        month=later_date.month,
        day=later_date.day
    )
    
    if later_date < comparison_date:
        year_diff -= 1
    
    return year_diff

if __name__ == '__main__':
    date_a = datetime(2000, 2, 29)
    date_b = datetime(2024, 2, 28)
    
    diff = calculate_full_year_difference(date_a, date_b)
    print(diff)