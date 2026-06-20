from datetime import date, timedelta

def is_valid_date(date_obj):
    if not isinstance(date_obj, date):
        raise ValueError("Input must be an instance of date.")

def count_weekdays(start_date, end_date):
    is_valid_date(start_date)
    is_valid_date(end_date)
    if start_date > end_date:
        raise ValueError("start_date must be before or equal to end_date.")
    
    weekdays = 0
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:
            weekdays += 1
        current_date += timedelta(days=1)
    return weekdays

if __name__ == '__main__':
    start_date = date(2023, 6, 1)
    end_date = date(2023, 8, 31)
    print(count_weekdays(start_date, end_date))