import datetime

def calculate_days_remaining(year, month, day=None):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if year < 1:
        raise ValueError("Year must be a positive integer")
    
    if month == 12:
        next_month_start = datetime.date(year + 1, 1, 1)
    else:
        next_month_start = datetime.date(year, month + 1, 1)
    
    last_day_of_month = next_month_start - datetime.timedelta(days=1)
    
    if day is None:
        current_date = datetime.date(year, month, 1)
        remaining = (last_day_of_month - current_date).days + 1
        return remaining
    
    if not (1 <= day <= last_day_of_month.day):
        raise ValueError("Day is out of range for the given month and year")
    
    current_date = datetime.date(year, month, day)
    remaining = (last_day_of_month - current_date).days + 1
    return remaining

if __name__ == '__main__':
    results = []
    results.append(calculate_days_remaining(2023, 2))
    results.append(calculate_days_remaining(2024, 2, 10))
    results.append(calculate_days_remaining(2023, 12, 25))
    for res in results:
        print(res)