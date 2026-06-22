from datetime import date

def is_weekend_or_holiday(date_str):
    holidays = {'2023-10-13', '2023-10-14', '2023-10-15'}
    return date.fromisoformat(date_str).weekday() >= 5 or date_str in holidays

def validate_date_format(date_str):
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    dates = ['2023-10-13', '2023-10-14', '2023-10-15']
    results = [is_weekend_or_holiday(date) for date in dates if validate_date_format(date)]
    print(results)