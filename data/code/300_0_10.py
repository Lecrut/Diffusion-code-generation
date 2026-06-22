from datetime import date

def days_remaining_in_month(current_date):
    if not isinstance(current_date, date):
        raise ValueError("Input must be a date object")
    
    _, month, year = current_date.year, current_date.month, current_date.year
    
    if month == 12:
        next_month = (year + 1, 1)
    else:
        next_month = (year, month + 1)
    
    first_day_of_next_month = date(*next_month)
    last_day_of_current_month = first_day_of_next_month - timedelta(days=1)
    
    return (last_day_of_current_month - current_date).days

if __name__ == '__main__':
    sample_date = date(2023, 4, 15)
    print(days_remaining_in_month(sample_date))