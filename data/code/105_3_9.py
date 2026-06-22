import datetime
import calendar

def compute_next_15th():
    base_date = datetime.date(2023, 3, 3)
    current_year = base_date.year
    current_month = base_date.month
    
    target_month = current_month + 1
    target_year = current_year
    
    if target_month > 12:
        target_month = 1
        target_year += 1
    
    target_date = datetime.date(target_year, target_month, 15)
    return target_date

if __name__ == '__main__':
    result = compute_next_15th()
    print(result)