from datetime import date

def is_valid_date(date_obj):
    try:
        date.fromisoformat(str(date_obj))
        return True
    except ValueError:
        return False

def years_between_dates(start_date: date, end_date: date) -> int:
    if not (is_valid_date(start_date) and is_valid_date(end_date)):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    if start_date > end_date:
        raise ValueError("Start date must be before end date.")
    
    year_diff = end_date.year - start_date.year
    month_day_diff = (end_date.month, end_date.day) < (start_date.month, start_date.day)
    return year_diff - month_day_diff

if __name__ == '__main__':
    start = date(2010, 5, 15)
    end = date(2023, 8, 20)
    print(years_between_dates(start, end))