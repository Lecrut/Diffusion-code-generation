from datetime import datetime

def compare_datetimes(first_dt: datetime, second_dt: datetime) -> str:
    if not isinstance(first_dt, datetime) or not isinstance(second_dt, datetime):
        raise ValueError("Both arguments must be datetime instances")
    if first_dt < second_dt:
        return "First is earlier"
    if first_dt > second_dt:
        return "Second is earlier"
    return "They are equal"

if __name__ == '__main__':
    dt_a = datetime(2024, 5, 10, 8, 30, 0)
    dt_b = datetime(2024, 5, 10, 8, 30, 0)
    output = compare_datetimes(dt_a, dt_b)
    print(output)