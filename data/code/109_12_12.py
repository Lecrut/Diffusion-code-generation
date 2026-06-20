from datetime import date

def days_and_percentage(year, month):
    if not (1 <= year <= 9999) or not (1 <= month <= 12):
        raise ValueError("Invalid year or month")
    
    first_day = date(year, month, 1)
    last_day = date(year, month + 1, 1) - timedelta(days=1)
    total_days = (last_day - first_day).days + 1
    today = date.today()
    
    if today < first_day:
        remaining_days = (first_day - today).days
        percentage_complete = 0.0
    elif today > last_day:
        remaining_days = 0
        percentage_complete = 100.0
    else:
        days_passed = (today - first_day).days + 1
        remaining_days = total_days - days_passed
        percentage_complete = (days_passed / total_days) * 100
    
    return remaining_days, f"{percentage_complete:.2f}%"

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 4
    remaining_days, completion_percentage = days_and_percentage(sample_year, sample_month)
    print(f"Remaining days: {remaining_days}")
    print(f"Completion percentage: {completion_percentage}")