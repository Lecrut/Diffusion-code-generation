from datetime import datetime
from typing import Tuple

VALIDATION_THRESHOLD_SECONDS = 0.0

def _validate_datetimes(start: datetime, end: datetime) -> None:
    if not isinstance(start, datetime):
        raise ValueError("start must be a datetime object")
    if not isinstance(end, datetime):
        raise ValueError("end must be a datetime object")
    diff_seconds = (end - start).total_seconds()
    if diff_seconds < VALIDATION_THRESHOLD_SECONDS:
        raise ValueError("end must be after start")

def compute_hours_elapsed(start: datetime, end: datetime) -> float:
    _validate_datetimes(start, end)
    total_seconds = (end - start).total_seconds()
    return total_seconds / 3600.0

if __name__ == '__main__':
    t_start = datetime(2024, 1, 1, 0, 0, 0)
    t_end = datetime(2024, 1, 1, 12, 30, 45)
    elapsed = compute_hours_elapsed(t_start, t_end)
    print(elapsed)