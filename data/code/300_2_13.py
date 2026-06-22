from dateutil.relativedelta import relativedelta
from datetime import datetime

def days_remaining(year, month):
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    
    today = datetime.now()
    target_date = datetime(year, month, 1) + relativedelta(months=1)
    remaining_days = (target_date - today).days
    
    return remaining_days

if __name__ == '__main__':
    print(days_remaining(2023, 4))