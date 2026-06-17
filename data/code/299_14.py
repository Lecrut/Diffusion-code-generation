import datetime
def check_weekday_weekend(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        day_of_week = date_obj.weekday()
        if day_of_week >= 5:
            print(f"The date {date_string} is a weekend.")
        else:
            print(f"The date {date_string} is a weekday.")
    except ValueError:
        print(f"Error: Invalid date format. Please enter the date in YYYY-MM-DD format.")
if __name__ == '__main__':
    sample_dates = [
        "2023-10-27",
        "2023-10-28",
        "2024-01-01",
        "2024-01-07"
    ]
    for date_str in sample_dates:
        check_weekday_weekend(date_str)