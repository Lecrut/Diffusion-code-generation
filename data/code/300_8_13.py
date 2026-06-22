from dateutil.relativedelta import relativedelta

def days_remaining(year, month):
    from datetime import datetime
    today = datetime.now()
    target_date = datetime(year, month, 1) + relativedelta(months=1)
    remaining_days = (target_date - today).days
    return remaining_days
if __name__ == '__main__':
    print(days_remaining(2023, 4))