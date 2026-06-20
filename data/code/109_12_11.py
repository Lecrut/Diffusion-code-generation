import datetime

def days_and_percentage(year, month):
    start_date = datetime.date(year, month, 1)
    if month == 2:
        end_date = datetime.date(year + (month // 12), (month % 12) + 1, 1) - datetime.timedelta(days=1)
    elif month in [4, 6, 9, 11]:
        end_date = datetime.date(year, month + 1, 1) - datetime.timedelta(days=1)
    else:
        end_date = datetime.date(year + (month // 12), (month % 12) + 1, 0)
    
    total_days = (end_date - start_date).days + 1
    today = datetime.date.today()
    if today < start_date or today > end_date:
        remaining_days = None
        percentage_complete = None
    else:
        remaining_days = (end_date - today).days
        percentage_complete = ((today - start_date).days / total_days) * 100
    
    return remaining_days, percentage_complete

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 4
    remaining_days, percentage_complete = days_and_percentage(sample_year, sample_month)
    print(f"Remaining days: {remaining_days}")
    print(f"Percentage complete: {percentage_complete:.2f}%")