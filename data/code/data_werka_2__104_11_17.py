from datetime import datetime

def calculate_days_difference(dt1: datetime, dt2: datetime) -> int:
    if dt1.tzinfo is not None:
        raise ValueError("Timezone-aware datetimes are not supported for naive comparison.")
    if dt2.tzinfo is not None:
        raise ValueError("Timezone-aware datetimes are not supported for naive comparison.")
    time_span = dt2 - dt1
    total_seconds = time_span.total_seconds()
    days_value = int(total_seconds / 86400)
    return days_value

if __name__ == '__main__':
    start_time = datetime(2024, 6, 1, 12, 0, 0)
    end_time = datetime(2024, 6, 15, 18, 30, 0)
    day_diff = calculate_days_difference(start_time, end_time)
    print(day_diff)