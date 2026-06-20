import calendar

def is_valid_date(year, month, day):
    try:
        calendar.weekday(year, month, day)
        return True
    except ValueError:
        return False

def check_weekdays(years_months_days):
    results = {}
    for date in years_months_days:
        if not is_valid_date(*date):
            results[date] = "Invalid date"
        else:
            weekday = calendar.weekday(*date) < 5
            results[date] = "Weekday" if weekday else "Not a weekday"
    return results

if __name__ == '__main__':
    dates_to_check = [
        (2023, 10, 23),
        (2023, 10, 24),
        (2023, 10, 28),
        (2023, 10, 29)
    ]
    results = check_weekdays(dates_to_check)
    for date, result in results.items():
        print(f"Is {date[0]}/{date[1]}/{date[2]} a weekday? {result}")