import datetime

def get_last_day_of_month(year, month):
    if month == 12:
        return datetime.date(year + 1, 1, 1) - datetime.timedelta(days=1)
    else:
        return datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)

def calculate_days_remaining(current_year, current_month):
    today = datetime.date.today()
    if current_year < today.year or (current_year == today.year and current_month < today.month):
        raise ValueError("Target date is before the current date.")
    
    last_day_of_current_month = get_last_day_of_month(today.year, today.month)
    target_date = datetime.date(current_year, current_month, 1)
    days_remaining = (target_date - last_day_of_current_month).days
    return days_remaining

if __name__ == '__main__':
    current_year = 2024
    current_month = 10
    print(calculate_days_remaining(current_year, current_month))