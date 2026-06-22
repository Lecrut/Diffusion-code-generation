from datetime import date
import calendar

def compute_year_span(reference_date: date, target_date: date) -> int:
    if not isinstance(reference_date, date) or not isinstance(target_date, date):
        raise ValueError("Inputs must be date instances")
    
    if reference_date == target_date:
        return 0
    
    if reference_date > target_date:
        reference_date, target_date = target_date, reference_date
    
    year_diff = target_date.year - reference_date.year
    
    if target_date.month < reference_date.month:
        year_diff -= 1
    elif target_date.month == reference_date.month:
        if target_date.day < reference_date.day:
            year_diff -= 1
            
    return year_diff

if __name__ == '__main__':
    start = date(1990, 1, 1)
    end = date(2023, 12, 31)
    result = compute_year_span(start, end)
    print(result)