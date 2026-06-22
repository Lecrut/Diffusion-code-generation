import calendar
import datetime

def validate_weekday(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        is_week = date_obj.weekday() < 5
        return is_week
    except ValueError:
        raise ValueError(f"Invalid date: {year}-{month}-{day}")

if __name__ == '__main__':
    valid_result = validate_weekday(2024, 5, 15)
    print(valid_result)
    invalid_result = validate_weekday(2024, 2, 30)
    print(invalid_result)