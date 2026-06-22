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
    day_of_week = date_obj.weekday()
    return day_of_week >= 5

def check_dates(dates):
    results = {date: is_weekend(date) for date in dates}
    return results

if __name__ == '__main__':
    sample_dates = [
        "2023-10-28",
        datetime.date(2023, 10, 29),
        "2023-10-30",
        datetime.date(2023, 10, 31)
    ]
    print(check_dates(sample_dates))