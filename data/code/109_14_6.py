from datetime import datetime, timedelta

def remaining_duration_in_month(date):
    year = date.year
    month = date.month
    if month == 12:
        next_month = (year + 1, 1)
    else:
        next_month = (year, month + 1)
    
    last_day_of_current_month = datetime(year, month, 1) + timedelta(days=31)
    first_day_of_next_month = datetime(next_month[0], next_month[1], 1)
    
    remaining_duration = first_day_of_next_month - date
    
    days = remaining_duration.days
    seconds = remaining_duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    
    return days, hours, minutes, seconds

if __name__ == '__main__':
    sample_date = datetime(2023, 10, 15)
    print(remaining_duration_in_month(sample_date))