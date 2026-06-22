import datetime

def check_weekend(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        if date_obj.weekday() >= 5:
            return True
        else:
            return False
    except ValueError:
        raise ValueError("Invalid date format. Please enter the date in YYYY-MM-DD format.")

if __name__ == '__main__':
    sample_dates = [
        "2023-10-27",
        "2023-10-28",
        "2024-01-01",
        "2024-01-07"
    ]

    for date in sample_dates:
        if check_weekend(date):
            print(f"The date {date} is a weekend.")
        else:
            print(f"The date {date} is a weekday.")