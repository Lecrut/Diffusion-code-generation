from datetime import datetime

def days_and_percentage(year, month):
    start_date = datetime(year, month, 1)
    if month == 12:
        end_date = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        end_date = datetime(year, month + 1, 1) - timedelta(days=1)
    
    total_days = (end_date - start_date).days + 1
    today = datetime.now()
    if today < start_date:
        remaining_days = (start_date - today).days
        percentage_complete = 0.0
    elif today > end_date:
        remaining_days = None
        percentage_complete = 100.0
    else:
        remaining_days = (end_date - today).days + 1
        percentage_complete = ((total_days - remaining_days) / total_days) * 100
    
    return remaining_days, percentage_complete

if __name__ == '__main__':
    year = 2023
    month = 4
    remaining_days, percentage_complete = days_and_percentage(year, month)
    print(f"Remaining days: {remaining_days}")
    print(f"Percentage complete: {percentage_complete:.2f}%")