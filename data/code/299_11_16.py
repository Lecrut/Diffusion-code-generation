import datetime
WEEKEND_DAYS = {5, 6}

def is_weekend(date_input):
    if isinstance(date_input, str):
        try:
            date_obj = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
        except ValueError:
            return False
    elif isinstance(date_input, datetime.date):
        date_obj = date_input
    else:
        raise TypeError('Input must be a datetime.date object or a string representation of a date.')
    return date_obj.weekday() in WEEKEND_DAYS
if __name__ == '__main__':
    dates_to_test = ['2023-10-28', datetime.date(2023, 10, 29), '2023-10-30', datetime.date(2023, 10, 31)]
    for date in dates_to_test:
        print(f'{date}: {is_weekend(date)}')