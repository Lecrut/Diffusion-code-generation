from datetime import datetime, timedelta

def remaining_duration_for_month(date):
    year = date.year
    month = date.month
    if month == 12:
        next_month = (year + 1, 1)
    else:
        next_month = (year, month + 1)
    
    last_day_of_current_month = datetime(year, month, 1) + timedelta(days=31)
    first_day_of_next_month = datetime(*next_month)
    
    remaining_duration = first_day_of_next_month - last_day_of_current_month
    
    days = remaining_duration.days
    hours = remaining_duration.seconds // 3600
    minutes = (remaining_duration.seconds % 3600) // 60
    seconds = remaining_duration.seconds % 60
    
    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 15)
    print(remaining_duration_for_month(sample_date))