import datetime

def days_left_in_month(year, month):
    if not (1 <= year <= 9999) or not (1 <= month <= 12):
        raise ValueError("Year must be between 1 and 9999 and month must be between 1 and 12")
    
    today = datetime.date.today()
    first_day_of_current_month = datetime.date(year, month, 1)
    last_day_of_current_month = first_day_of_current_month.replace(day=28) + datetime.timedelta(days=4)
    days_in_month = (last_day_of_current_month - first_day_of_current_month).days
    
    if today > first_day_of_current_month:
        days_left = days_in_month - (today.day - 1)
    else:
        days_left = days_in_month
    
    return days_left

if __name__ == '__main__':
    year = 2023
    month = 10
    days_left = days_left_in_month(year, month)
    print(days_left)