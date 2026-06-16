import datetime
def check_weekday_weekend(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
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
        "2023-10-29",
        "2023-10-30",
        "2023-10-31",
        "2023-11-05"
    ]
    for date_str in sample_dates:
        check_weekday_weekend(date_str)