from datetime import date, timedelta

def get_next_month(year, month):
    if not isinstance(year, int) or not isinstance(month, int):
        raise ValueError('Year and month must be integers.')
    if month < 1 or month > 12:
        raise ValueError('Month must be between 1 and 12.')
    try:
        next_date = date(year, month, 1)
        if next_date.month == 12:
            next_year = year + 1
            next_month = 1
        else:
            next_year = year
            next_month = month + 1
        return date(next_year, next_month, 1) - timedelta(days=1)
    except ValueError:
        raise ValueError('Invalid date format.')
if __name__ == '__main__':
    print(get_next_month(2023, 1))
    print(get_next_month(2023, 5))
    print(get_next_month(2023, 12))