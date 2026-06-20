from datetime import datetime

def days_and_percentage(year, month):
    start_date = datetime(year, month, 1)
    if month == 12:
        end_date = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        end_date = datetime(year, month + 1, 1) - timedelta(days=1)
    
    total_days = (end_date - start_date).days + 1
    today = datetime.now()
    if today > end_date:
        remaining_days = 0
    elif today < start_date:
        remaining_days = (end_date - today).days + 1
    else:
        remaining_days = 0
    
    percentage_complete = ((total_days - remaining_days) / total_days) * 100 if total_days > 0 else 100
    
    return remaining_days, percentage_complete

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 4
    result = days_and_percentage(sample_year, sample_month)
    print(f"Remaining Days: {result[0]}, Percentage Complete: {result[1]:.2f}%")