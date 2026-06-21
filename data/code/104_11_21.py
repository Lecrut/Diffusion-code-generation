from datetime import datetime

DAY_UNITS = 86400

def get_days_delta(first: datetime, second: datetime) -> int:
    if first.tzinfo is not None or second.tzinfo is not None:
        raise ValueError("Timezone-aware datetimes are not supported.")
    total_seconds = (second - first).total_seconds()
    return int(total_seconds // DAY_UNITS)

if __name__ == '__main__':
    start_dt = datetime(2023, 6, 1, 0, 0, 0)
    end_dt = datetime(2023, 6, 15, 12, 30, 0)
    delta = get_days_delta(start_dt, end_dt)
    print(delta)