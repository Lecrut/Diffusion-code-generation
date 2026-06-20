from datetime import date, timedelta

def is_valid_date(year, month, day):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def count_weekdays(start_year, start_month, start_day, end_year, end_month, end_day):
    if not (is_valid_date(start_year, start_month, start_day) and is_valid_date(end_year, end_month, end_day)):
        raise ValueError("Both start_date and end_date must be valid dates.")
    if date(start_year, start_month, start_day) > date(end_year, end_month, end_day):
        raise ValueError("start_date must be before or equal to end_date.")
    
    start_date = date(start_year, start_month, start_day)
    end_date = date(end_year, end_month, end_day)
    weekdays = 0
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:
            weekdays += 1
        current_date += timedelta(days=1)
    return weekdays

if __name__ == '__main__':
    start_year, start_month, start_day = 2023, 6, 1
    end_year, end_month, end_day = 2023, 8, 31
    print(count_weekdays(start_year, start_month, start_day, end_year, end_month, end_day))