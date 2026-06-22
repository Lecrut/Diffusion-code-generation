import datetime

def check_weekday_weekend(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        day_of_week = date_obj.weekday()
        if day_of_week >= 5:
            return True
        else:
            return False
    except ValueError:
        raise ValueError("Error: Invalid date format. Please enter the date in YYYY-MM-DD format.")

def print_weekend_status(date_string):
    is_weekend = check_weekday_weekend(date_string)
    if is_weekend:
        print(f"The date {date_string} is a weekend.")
    else:
        print(f"The date {date_string} is a weekday.")

if __name__ == '__main__':
    sample_dates = [
        "2023-10-27",
        "2023-10-28",
        "2024-01-01",
        "2024-01-07"
    ]

    for date in sample_dates:
        print_weekend_status(date)