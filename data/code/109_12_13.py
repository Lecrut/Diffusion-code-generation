from datetime import date

def days_and_percentage(year, month):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    first_day = date(year, month, 1)
    last_day = date(year, month + 1, 1) - timedelta(days=1)
    total_days = (last_day - first_day).days + 1
    today = date.today()
    days_passed = (today - first_day).days + 1 if today >= first_day else 0
    
    remaining_days = max(0, last_day - today).days
    percentage_complete = round((days_passed / total_days) * 100, 2)
    
    return remaining_days, percentage_complete

if __name__ == '__main__':
    year = 2023
    month = 4
    remaining_days, percentage_complete = days_and_percentage(year, month)
    print(f"Remaining days: {remaining_days}")
    print(f"Percentage complete: {percentage_complete}%")