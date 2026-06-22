from datetime import datetime

def is_first_earlier(date_a: datetime, date_b: datetime) -> bool:
    if not isinstance(date_a, datetime):
        raise ValueError("date_a must be a datetime object")
    if not isinstance(date_b, datetime):
        raise ValueError("date_b must be a datetime object")
    return date_a < date_b

def validate_date_input(dt_val: datetime) -> bool:
    if dt_val is None:
        raise ValueError("Input datetime cannot be None")
    if dt_val.microsecond < 0 or dt_val.microsecond > 999999:
        raise ValueError("Invalid microsecond value")
    if dt_val.second < 0 or dt_val.second > 59:
        raise ValueError("Invalid second value")
    if dt_val.minute < 0 or dt_val.minute > 59:
        raise ValueError("Invalid minute value")
    if dt_val.hour < 0 or dt_val.hour > 23:
        raise ValueError("Invalid hour value")
    if dt_val.day < 1 or dt_val.day > 31:
        raise ValueError("Invalid day value")
    if dt_val.month < 1 or dt_val.month > 12:
        raise ValueError("Invalid month value")
    return True

if __name__ == '__main__':
    start_dt = datetime(2024, 1, 15, 10, 30, 0)
    end_dt = datetime(2024, 1, 16, 10, 30, 0)
    validate_date_input(start_dt)
    validate_date_input(end_dt)
    outcome = is_first_earlier(start_dt, end_dt)
    print(outcome)