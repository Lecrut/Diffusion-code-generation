from datetime import date

def days_and_percentage(year, month):
    start_date = date(year, month, 1)
    if month == 12:
        end_date = date(year + 1, 1, 1) - timedelta(days=1)
    else:
        end_date = date(year, month + 1, 1) - timedelta(days=1)
    
    total_days = (end_date - start_date).days + 1
    today = date.today()
    if today < start_date:
        remaining_days = (start_date - today).days
        percentage_complete = 0
    elif today > end_date:
        remaining_days = 0
        percentage_complete = 100
    else:
        elapsed_days = (today - start_date).days + 1
        remaining_days = total_days - elapsed_days
        percentage_complete = (elapsed_days / total_days) * 100
    
    return remaining_days, percentage_complete

if __name__ == '__main__':
    year = 2023
    month = 4
    remaining_days, percentage_complete = days_and_percentage(year, month)
    print(f"Remaining days: {remaining_days}")
    print(f"Percentage complete: {percentage_complete:.2f}%")