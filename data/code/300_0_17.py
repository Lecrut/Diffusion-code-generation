from datetime import date, timedelta

def days_remaining_in_month(current_date):
    if not isinstance(current_date, date):
        raise ValueError("Input must be a date object")
    
    next_month = current_date.replace(day=28) + timedelta(days=4)
    return (next_month - next_month.replace(day=1)).days

if __name__ == '__main__':
    sample_date = date(2023, 9, 15)
    print(days_remaining_in_month(sample_date))