import calendar
from datetime import date

def verify_workday(target_date):
    if not isinstance(target_date, date):
        raise ValueError("Expected a date instance")
    try:
        day_code = calendar.weekday(target_date.year, target_date.month, target_date.day)
        return day_code < 5
    except AttributeError as err:
        raise ValueError("Invalid date components") from err

if __name__ == '__main__':
    test_dt = date(2024, 2, 14)
    output = verify_workday(test_dt)
    print(output)