from datetime import datetime, timedelta

def calculate_days_difference(dt1: datetime, dt2: datetime) -> int:
    if dt1.tzinfo is not None or dt2.tzinfo is not None:
        raise ValueError("Timezone-aware datetimes are not supported for naive comparison.")
    delta = dt2 - dt1
    return delta.days

if __name__ == '__main__':
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    result = calculate_days_difference(start_date, end_date)
    print(result)