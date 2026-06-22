from dateutil.relativedelta import relativedelta
from datetime import datetime

def days_remaining_in_month(year, month):
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    
    end_of_month = datetime(year, month, 1) + relativedelta(months=1) - relativedelta(days=1)
    today = datetime.now()
    remaining_days = (end_of_month - today).days
    return remaining_days

if __name__ == '__main__':
    print(days_remaining_in_month(2023, 4))