import datetime

def is_weekend(date_input):
    if isinstance(date_input, str):
        try:
            date_obj = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
        except ValueError:
            return False
    elif isinstance(date_input, datetime.date):
        date_obj = date_input
    else:
        return False
    return date_obj.weekday() >= 5
if __name__ == '__main__':
    dates_to_test = [datetime.date(2023, 10, 28), '2023-10-29', datetime.date(2023, 10, 30), '2023-10-31']
    results = {date: is_weekend(date) for date in dates_to_test}
    print(results)