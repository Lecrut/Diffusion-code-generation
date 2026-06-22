from datetime import datetime, timedelta

SECONDS_IN_DAY = 86400

def get_days_delta(first: datetime, second: datetime) -> int:
    if first.tzinfo is not None:
        raise ValueError("First datetime must be naive.")
    if second.tzinfo is not None:
        raise ValueError("Second datetime must be naive.")
    seconds_diff = (second - first).total_seconds()
    return int(seconds_diff / SECONDS_IN_DAY)

if __name__ == '__main__':
    date_a = datetime(2023, 3, 1, 0, 0, 0)
    date_b = datetime(2023, 3, 15, 12, 0, 0)
    diff = get_days_delta(date_a, date_b)
    print(diff)