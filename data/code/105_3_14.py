from datetime import date

def is_valid_date(year, month):
    if year < 1 or month < 1 or month > 12:
        return False
    return True

def next_15th_day_of_month(start_date):
    if not is_valid_date(start_date.year, start_date.month):
        raise ValueError("Invalid date")
    
    current_year = start_date.year
    current_month = start_date.month + 1
    
    if current_month > 12:
        current_year += 1
        current_month = 1
    
    target_date = date(current_year, current_month, 15)
    return target_date

if __name__ == '__main__':
    sample_date = date(2023, 3, 3)
    result = next_15th_day_of_month(sample_date)
    print(result)