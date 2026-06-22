import datetime

WEEKEND_DAYS = (5, 6)

def check_weekdays(*date_strings):
    for date_string in date_strings:
        try:
            date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
            day_of_week = date_obj.weekday()
            result = "weekend" if day_of_week in WEEKEND_DAYS else "weekday"
            print(f"The date {date_string} is a {result}.")
        except ValueError:
            print(f"Error: Invalid date format. Please enter the date in YYYY-MM-DD format.")

if __name__ == '__main__':
    sample_dates = [
        "2023-10-27",
        "2023-10-28",
        "2024-01-01",
        "2024-01-07"
    ]
    check_weekdays(*sample_dates)