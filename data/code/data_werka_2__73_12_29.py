from datetime import datetime, timezone

def compute_seconds_delta(start_iso: str, end_iso: str) -> float:
    try:
        start_dt = datetime.fromisoformat(start_iso)
        end_dt = datetime.fromisoformat(end_iso)
    except ValueError as e:
        raise ValueError(f"Invalid ISO 8601 format: {e}") from e

    if start_dt.tzinfo is None:
        start_dt = start_dt.replace(tzinfo=timezone.utc)
    if end_dt.tzinfo is None:
        end_dt = end_dt.replace(tzinfo=timezone.utc)

    delta = end_dt - start_dt
    return delta.total_seconds()

if __name__ == '__main__':
    ts_start = "2023-01-01T00:00:00+00:00"
    ts_end = "2023-01-01T00:00:01+00:00"
    diff = compute_seconds_delta(ts_start, ts_end)
    print(diff)