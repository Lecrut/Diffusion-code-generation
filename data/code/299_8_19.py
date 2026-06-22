from datetime import date

def is_weekend_or_holiday(date_str):
    weekend_days = {5, 6}
    holidays = {'2023-10-13', '2023-10-14', '2023-10-15'}
    given_date = date.fromisoformat(date_str)
    return given_date.weekday() in weekend_days or date_str in holidays
if __name__ == '__main__':
    print(is_weekend_or_holiday('2023-10-13'))
    print(is_weekend_or_holiday('2023-10-14'))
    print(is_weekend_or_holiday('2023-10-15'))