from datetime import datetime

def calculate_days_difference(dt_a: datetime, dt_b: datetime) -> int:
    if dt_a.tzinfo is not None:
        raise ValueError("First datetime must be timezone-naive.")
    if dt_b.tzinfo is not None:
        raise ValueError("Second datetime must be timezone-naive.")
    if not isinstance(dt_a, datetime):
        raise ValueError("First argument must be a datetime object.")
    if not isinstance(dt_b, datetime):
        raise ValueError("Second argument must be a datetime object.")
    delta = dt_b - dt_a
    return delta.days

if __name__ == '__main__':
    date_one = datetime(2024, 2, 1, 0, 0, 0)
    date_two = datetime(2024, 2, 15, 12, 30, 0)
    diff = calculate_days_difference(date_one, date_two)
    print(diff)