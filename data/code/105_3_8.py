import datetime
import calendar

def next_fifteenth_month_reference():
    reference_date = datetime.date(2023, 3, 3)
    current_year = reference_date.year
    current_month = reference_date.month
    
    target_month = current_month + 1
    target_year = current_year
    
    if target_month > 12:
        target_month = 1
        target_year += 1
        
    target_day = 15
    next_fifteenth = datetime.date(target_year, target_month, target_day)
    
    return next_fifteenth

if __name__ == '__main__':
    result = next_fifteenth_month_reference()
    print(result)