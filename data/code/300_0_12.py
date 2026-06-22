from datetime import date

def days_remaining_in_month(current_date):
    if not isinstance(current_date, date):
        raise ValueError("Input must be a date object")
    
    _, month, year = current_date.month, current_date.year
    next_month = (month % 12) + 1
    next_year = year + (next_month == 1)
    last_day_of_next_month = date(next_year, next_month, 1) - timedelta(days=1)
    
    return (last_day_of_next_month - current_date).days

if __name__ == '__main__':
    sample_date = date(2023, 4, 15)
    print(days_remaining_in_month(sample_date))