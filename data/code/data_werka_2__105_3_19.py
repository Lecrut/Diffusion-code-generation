from datetime import date
import calendar

def find_next_15th(reference_date: date) -> date:
    if reference_date.day < 15:
        return date(reference_date.year, reference_date.month, 15)
    
    next_month = reference_date.month + 1
    next_year = reference_date.year
    
    if next_month > 12:
        next_month = 1
        next_year += 1
        
    return date(next_year, next_month, 15)

if __name__ == '__main__':
    start = date(2023, 3, 3)
    computed = find_next_15th(start)
    print(computed)