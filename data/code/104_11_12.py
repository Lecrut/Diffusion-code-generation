from datetime import datetime

def get_days_between(dt_a: datetime, dt_b: datetime) -> int:
    if dt_a.tzinfo is not None or dt_b.tzinfo is not None:
        raise ValueError("Timezone-aware datetimes are not supported for naive comparison.")
    time_diff = dt_b - dt_a
    return time_diff.days

if __name__ == '__main__':
    first_date = datetime(2024, 2, 1, 8, 0, 0)
    second_date = datetime(2024, 2, 15, 18, 0, 0)
    diff = get_days_between(first_date, second_date)
    print(diff)