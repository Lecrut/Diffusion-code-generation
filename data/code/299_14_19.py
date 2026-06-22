import datetime

def is_weekend(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
        day_of_week = date_obj.weekday()
        return day_of_week >= 5
    except ValueError:
        raise ValueError("Invalid date format. Please enter the date in YYYY-MM-DD format.")

def check_dates(dates):
    results = {}
    for date_str in dates:
        try:
            if is_weekend(date_str):
                results[date_str] = "weekend"
            else:
                results[date_str] = "weekday"
        except ValueError as e:
            results[date_str] = str(e)
    return results

if __name__ == '__main__':
    sample_dates = [
        "2023-10-27",
        "2023-10-28",
        "2024-01-01",
        "2024-01-07"
    ]
    
    results = check_dates(sample_dates)
    for date, result in results.items():
        print(f"The date {date} is a {result}.")