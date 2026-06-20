from datetime import date

def days_and_percentage(year, month):
    first_day = date(year, month, 1)
    if month == 12:
        last_day = date(year + 1, 1, 1) - timedelta(days=1)
    else:
        last_day = date(year, month + 1, 1) - timedelta(days=1)
    
    remaining_days = (last_day - date.today()).days
    percentage_completed = ((date.today() - first_day).days / (last_day - first_day).days) * 100
    
    return remaining_days, round(percentage_completed, 2)

if __name__ == '__main__':
    year = 2023
    month = 4
    remaining_days, percentage_completed = days_and_percentage(year, month)
    print(f"Remaining days: {remaining_days}")
    print(f"Percentage completed: {percentage_completed}%")