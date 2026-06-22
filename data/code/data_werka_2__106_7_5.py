from datetime import date
import calendar

def calculate_full_years(start_date: date, end_date: date) -> int:
    if not isinstance(start_date, date) or not isinstance(end_date, date):
        raise ValueError("Inputs must be date objects")
    if start_date > end_date:
        raise ValueError("start_date must be before or equal to end_date")
    
    if start_date == end_date:
        return 0
    
    year_diff = end_date.year - start_date.year
    
    if year_diff == 0:
        return 0
    
    potential_anniversary_year = start_date.year + year_diff
    potential_anniversary = date(potential_anniversary_year, start_date.month, start_date.day)
    
    if potential_anniversary > end_date:
        return year_diff - 1
    
    return year_diff

if __name__ == '__main__':
    start = date(1990, 5, 15)
    end = date(2023, 5, 14)
    result = calculate_full_years(start, end)
    print(result)