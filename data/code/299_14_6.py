import datetime

def is_weekend(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
        day_of_week = date_obj.weekday()
        return day_of_week >= 5
    except ValueError:
        raise ValueError("Invalid date format. Please enter the date in YYYY-MM-DD format.")

def check_weekdays_weekends(date_strings):
    results = {}
    for date_string in date_strings:
        is_weekend_status = is_weekend(date_string)
        results[date_string] = "Weekend" if is_weekend_status else "Weekday"
    return results

if __name__ == '__main__':
    sample_dates = [
        "2023-10-27",
        "2023-10-28",
        "2024-01-01",
        "2024-01-07"
    ]
    
    results = check_weekdays_weekends(sample_dates)
    for date_string, status in results.items():
        print(f"The date {date_string} is a {status}.")