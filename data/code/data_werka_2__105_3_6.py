from datetime import date
import calendar

def get_next_15th_after_reference(reference: date) -> date:
    if not isinstance(reference, date):
        raise ValueError("Input must be a date object")
    
    next_month = reference.month + 1
    next_year = reference.year
    
    if next_month > 12:
        next_month = 1
        next_year += 1
    
    return date(next_year, next_month, 15)

if __name__ == '__main__':
    hardcoded_date = date(2023, 3, 3)
    result = get_next_15th_after_reference(hardcoded_date)
    print(result)