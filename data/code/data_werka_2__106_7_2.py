from datetime import date

def get_full_years_between(start_date: date, end_date: date) -> int:
    if not isinstance(start_date, date) or not isinstance(end_date, date):
        raise ValueError("Inputs must be date objects")
    if start_date > end_date:
        raise ValueError("start_date must be before or equal to end_date")
    
    year_diff = end_date.year - start_date.year
    if year_diff == 0:
        return 0
    
    current_year = start_date.year + year_diff
    potential_anniversary = date(current_year, start_date.month, start_date.day)
    
    if potential_anniversary > end_date:
        return year_diff - 1
    
    return year_diff

if __name__ == '__main__':
    start = date(1990, 5, 15)
    end = date(2023, 5, 14)
    result = get_full_years_between(start, end)
    print(result)