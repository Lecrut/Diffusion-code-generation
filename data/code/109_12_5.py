from datetime import date

def days_and_percentage(year, month):
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    
    first_day = date(year, month, 1)
    last_day = date(year, month + 1, 1) - timedelta(days=1)
    total_days = (last_day - first_day).days + 1
    today = date.today()
    days_passed = (today - first_day).days + 1 if today >= first_day else 0
    
    remaining_days = max(0, total_days - days_passed)
    percentage_complete = (days_passed / total_days) * 100 if total_days > 0 else 0
    
    return remaining_days, round(percentage_complete, 2)

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 4
    remaining_days, percentage_complete = days_and_percentage(sample_year, sample_month)
    print(f"Remaining days: {remaining_days}")
    print(f"Percentage complete: {percentage_complete}%")