import datetime

def check_weekday_weekend(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        day_of_week = date_obj.weekday()
        return "weekend" if day_of_week >= 5 else "weekday"
    except ValueError:
        return "Invalid date format. Please enter the date in YYYY-MM-DD format."

if __name__ == '__main__':
    sample_dates = [
        "2023-10-27",
        "2023-10-28",
        "2024-01-01",
        "2024-01-07"
    ]
    
    results = {date: check_weekday_weekend(date) for date in sample_dates}
    for date, result in results.items():
        print(f"The date {date} is a {result}.")