import pandas as pd

def is_valid_date(date_str):
    try:
        pd.to_datetime(date_str)
        return True
    except ValueError:
        return False

def calculate_remaining_days(date_str):
    if not is_valid_date(date_str):
        raise ValueError("Invalid date format")
    
    date = pd.to_datetime(date_str)
    last_day_of_month = pd.Timestamp(year=date.year, month=date.month, day=31)
    if date.month == 2:
        last_day_of_month = last_day_of_month.replace(day=28) + pd.DateOffset(days=4)
        last_day_of_month -= pd.DateOffset(days=last_day_of_month.day % 7)
    
    return (last_day_of_month - date).days

if __name__ == '__main__':
    sample_date = '2023-10-15'
    print(calculate_remaining_days(sample_date))