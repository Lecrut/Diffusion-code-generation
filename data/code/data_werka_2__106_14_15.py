from datetime import datetime

YEARS_IN_DECADE = 10
YEARS_IN_CENTURY = 100

def calculate_year_difference(date_a: datetime, date_b: datetime) -> int:
    year_a = date_a.year
    year_b = date_b.year
    
    if year_a == year_b:
        return 0
        
    month_a = date_a.month
    day_a = date_a.day
    month_b = date_b.month
    day_b = date_b.day
    
    is_date_b_later = year_b > year_a
    if not is_date_b_later:
        return calculate_year_difference(date_b, date_a)
        
    year_diff = year_b - year_a
    
    if month_b > month_a:
        return year_diff
    if month_b == month_a and day_b >= day_a:
        return year_diff
        
    return year_diff - 1

if __name__ == '__main__':
    start_date = datetime(2010, 12, 31)
    end_date = datetime(2020, 1, 1)
    diff = calculate_year_difference(start_date, end_date)
    print(diff)