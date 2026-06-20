import datetime

def validate_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError('Invalid date format. Please provide a date in the format YYYY-MM-DD.')

def calculate_next_month(start_date):
    if start_date is None:
        return None
    year = start_date.year
    month = start_date.month
    day = start_date.day
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    try:
        return datetime.date(next_year, next_month, day)
    except ValueError:
        if month == 2 and day > 28:
            return datetime.date(next_year, next_month, 28)
        elif month in [4, 6, 9, 11] and day > 30:
            return datetime.date(next_year, next_month, 30)
        else:
            raise ValueError('Unexpected error calculating next month.')
if __name__ == '__main__':
    start_date_str = '2023-12-31'
    start_date = validate_date(start_date_str)
    next_date = calculate_next_month(start_date)
    print(next_date.strftime('%Y-%m-%d'))