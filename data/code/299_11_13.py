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
    weekday = date_obj.weekday()
    return weekday >= 5

def check_dates(dates):
    results = []
    for date in dates:
        result = is_weekend(date)
        results.append((date, "Weekend" if result else "Not Weekend"))
    return results

if __name__ == '__main__':
    sample_dates = [
        datetime.date(2023, 10, 28),
        "2023-10-29",
        datetime.date(2023, 10, 30),
        "2023-10-31"
    ]
    results = check_dates(sample_dates)
    for date, result in results:
        print(f"{date}: {result}")