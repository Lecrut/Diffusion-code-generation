import datetime

def is_weekend(date_input):
    if isinstance(date_input, datetime.date):
        return date_input.weekday() >= 5
    elif isinstance(date_input, str):
        try:
            date_obj = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
            return date_obj.weekday() >= 5
        except ValueError:
            return False
    else:
        return False

if __name__ == '__main__':
    dates_to_test = [
        datetime.date(2023, 10, 27),
        "2023-10-28",
        datetime.date(2023, 10, 29),
        "2023-10-30"
    ]

    for date in dates_to_test:
        result = is_weekend(date)
        print(f"Is {date} a weekend? {'Yes' if result else 'No'}")