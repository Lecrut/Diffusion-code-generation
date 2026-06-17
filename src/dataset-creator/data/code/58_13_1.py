import datetime
def calculate_date_difference(days_a: int | None = None, days_b: int | None = None) -> float:
    if not (days_a is not None and 0 <= days_a < 365):
        raise ValueError("Invalid date A")
    if not (days_b is not None and 0 <= days_b < 365):
        raise ValueError("Invalid date B")
    base_date = datetime.date(2001, 4, 7)
    try:
        date_a = base_date + datetime.timedelta(days=days_a)
        date_b = base_date + datetime.timedelta(days=days_b)
        diff_days = abs((date_a - date_b).days)
        return float(diff_days)
    except OverflowError as e:
        raise ValueError(f"Date overflow occurred. {e}")
if __name__ == '__main__':
    result = calculate_date_difference(days_a=15, days_b=30)
    print(result)