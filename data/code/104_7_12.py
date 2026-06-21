from datetime import datetime, timezone, timedelta

HOURS_PER_DAY = 24
SECONDS_PER_HOUR = 3600
UTC = timezone.utc

def compute_time_delta_hours(reference: datetime, target: datetime) -> float:
    if reference.tzinfo is None or target.tzinfo is None:
        raise ValueError("Both datetime objects must be timezone-aware")
    ref_utc = reference.astimezone(UTC)
    tgt_utc = target.astimezone(UTC)
    diff = ref_utc - tgt_utc
    return diff.total_seconds() / SECONDS_PER_HOUR

if __name__ == '__main__':
    start = datetime(2023, 11, 15, 8, 0, 0, tzinfo=UTC)
    end = datetime(2023, 11, 15, 14, 30, 0, tzinfo=UTC)
    delta = compute_time_delta_hours(start, end)
    print(delta)