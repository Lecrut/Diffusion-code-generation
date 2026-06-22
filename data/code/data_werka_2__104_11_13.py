from datetime import datetime, timezone

def calculate_days_difference(dt1: datetime, dt2: datetime) -> int:
    if dt1.tzinfo is not None or dt2.tzinfo is not None:
        raise ValueError("Timezone-aware datetimes are not supported for naive comparison")
    delta = dt2 - dt1
    return delta.days

if __name__ == '__main__':
    dt_start = datetime(2023, 1, 1, 12, 0, 0)
    dt_end = datetime(2023, 1, 10, 12, 0, 0)
    result = calculate_days_difference(dt_start, dt_end)
    print(result)