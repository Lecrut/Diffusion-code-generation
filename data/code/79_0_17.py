import datetime
DAYS_IN_MONTH = 31

def calculate_next_month(start_date):
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
            raise ValueError('Invalid date')
if __name__ == '__main__':
    start_date_str = '2023-12-31'
    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    next_date = calculate_next_month(start_date)
    print(next_date.strftime('%Y-%m-%d'))