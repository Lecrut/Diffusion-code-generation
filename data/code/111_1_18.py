from datetime import date, timedelta

def add_days_to_july_4():
    base_year = 2024
    base_month = 7
    base_day = 4
    days_to_add = 30
    
    if base_year < 1 or base_year > 9999:
        raise ValueError("Year out of range")
    if base_month < 1 or base_month > 12:
        raise ValueError("Month out of range")
    if base_day < 1:
        raise ValueError("Day out of range")
        
    try:
        start_date = date(base_year, base_month, base_day)
    except ValueError as e:
        raise ValueError(f"Invalid date: {e}")
        
    delta = timedelta(days=days_to_add)
    result_date = start_date + delta
    return result_date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    print(add_days_to_july_4())