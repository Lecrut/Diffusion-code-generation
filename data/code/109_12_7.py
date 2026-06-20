from datetime import date

def days_and_percentage(year, month):
    if not (1 <= month <= 12) or not (1900 <= year <= 2100):
        raise ValueError("Invalid year or month")
    
    first_day = date(year, month, 1)
    if month == 12:
        last_day = date(year + 1, 1, 1) - timedelta(days=1)
    else:
        last_day = date(year, month + 1, 1) - timedelta(days=1)
    
    total_days = (last_day - first_day).days + 1
    today = date.today()
    if today < first_day:
        remaining_days = (first_day - today).days
        percentage_complete = 0
    elif today > last_day:
        remaining_days = 0
        percentage_complete = 100
    else:
        remaining_days = (last_day - today).days
        percentage_complete = ((total_days - remaining_days) / total_days) * 100
    
    return remaining_days, round(percentage_complete, 2)

if __name__ == '__main__':
    year = 2023
    month = 4
    remaining_days, percentage_complete = days_and_percentage(year, month)
    print(f"Remaining days: {remaining_days}")
    print(f"Percentage complete: {percentage_complete}%")