from datetime import date, timedelta

def next_fifteenth_after_reference():
    reference_date = date(2023, 3, 3)
    current_year = reference_date.year
    current_month = reference_date.month
    
    if current_month < 3:
        target_month = 3
        target_year = current_year
    elif current_month == 3:
        if reference_date.day <= 15:
            target_month = 3
            target_year = current_year
        else:
            target_month = 4
            target_year = current_year
    else:
        target_month = current_month + 1
        target_year = current_year
        
        if target_month > 12:
            target_month = 1
            target_year = current_year + 1
            
    target_date = date(target_year, target_month, 15)
    return target_date

if __name__ == '__main__':
    result = next_fifteenth_after_reference()
    print(result)