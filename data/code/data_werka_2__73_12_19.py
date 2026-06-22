from datetime import datetime, timezone
from typing import Union

def compute_iso_delta_seconds(start_iso: str, end_iso: str) -> Union[int, float]:
    try:
        start_dt = datetime.fromisoformat(start_iso)
        end_dt = datetime.fromisoformat(end_iso)
    except ValueError as e:
        raise ValueError(f"Invalid ISO 8601 format: {e}") from None

    if start_dt.tzinfo is None:
        start_dt = start_dt.replace(tzinfo=timezone.utc)
    if end_dt.tzinfo is None:
        end_dt = end_dt.replace(tzinfo=timezone.utc)

    delta = end_dt - start_dt
    return delta.total_seconds()

if __name__ == '__main__':
    ts_a = "2024-01-15T10:00:00Z"
    ts_b = "2024-01-15T10:00:05.123456Z"
    diff = compute_iso_delta_seconds(ts_a, ts_b)
    print(diff)