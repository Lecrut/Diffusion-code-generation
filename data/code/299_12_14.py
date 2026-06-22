import datetime

def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def check_weekend_status(*dates):
    results = {}
    for date in dates:
        if not is_valid_date(date):
            results[date] = "Invalid date"
        else:
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            weekday = date_obj.weekday()
            results[date] = "Weekend" if weekday >= 5 else "Not a weekend"
    return results

if __name__ == '__main__':
    dates_to_check = ["2023-10-28", "2023-10-29", "2023-10-30", "2023-10-31", "2023-11-05"]
    weekend_status = check_weekend_status(*dates_to_check)
    for date, status in weekend_status.items():
        print(f"{date} is {status}")