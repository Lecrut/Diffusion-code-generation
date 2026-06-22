from datetime import date
import calendar

def year_difference(start_date: date, end_date: date) -> int:
    if not isinstance(start_date, date) or not isinstance(end_date, date):
        raise ValueError("Inputs must be date objects")
    
    years = end_date.year - start_date.year
    
    if years == 0:
        return 0
    
    if years > 0:
        next_anniversary = date(end_date.year - years + 1, start_date.month, start_date.day)
        if end_date < next_anniversary:
            years -= 1
    else:
        prev_anniversary = date(start_date.year + years - 1, end_date.month, end_date.day)
        if start_date > prev_anniversary:
            years += 1
            
    return years

if __name__ == '__main__':
    d1 = date(2020, 2, 29)
    d2 = date(2023, 2, 28)
    result = year_difference(d1, d2)
    print(result)