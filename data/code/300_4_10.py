import pandas as pd

def calculate_remaining_days(date):
    try:
        date_obj = pd.to_datetime(date)
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'")
    
    end_of_month = pd.Timestamp(year=date_obj.year, month=date_obj.month, day=31)
    if date_obj.month == 2:
        end_of_month = end_of_month.replace(day=28) + pd.DateOffset(days=4)
        end_of_month -= pd.DateOffset(days=end_of_month.day % 7)
    
    return (end_of_month - date_obj).days

if __name__ == '__main__':
    sample_date = '2023-10-15'
    print(calculate_remaining_days(sample_date))