from datetime import date, timedelta

def next_15th_after_reference():
    reference_date = date(2023, 3, 3)
    current_year = reference_date.year
    current_month = reference_date.month + 1
    
    if current_month > 12:
        current_month = 1
        current_year += 1
        
    target_date = date(current_year, current_month, 15)
    return target_date

if __name__ == '__main__':
    result = next_15th_after_reference()
    print(result)