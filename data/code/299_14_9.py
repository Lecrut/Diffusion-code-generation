import datetime

def is_valid_date(date_string):
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def check_weekday_weekend(date_string):
    if not is_valid_date(date_string):
        print(f"Error: Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return
    
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    day_of_week = date_obj.weekday()
    
    if day_of_week >= 5:
        print(f"The date {date_string} is a weekend.")
    else:
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        print(f"The date {date_string} is a weekday ({days[day_of_week]}).")

if __name__ == '__main__':
    sample_dates = [
        "2023-10-27",
        "2023-10-28",
        "2024-01-01",
        "2024-01-07"
    ]
    
    for date in sample_dates:
        check_weekday_weekend(date)