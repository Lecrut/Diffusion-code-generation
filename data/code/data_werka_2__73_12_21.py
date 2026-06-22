from datetime import datetime, timezone

def compute_seconds_delta(start_iso: str, end_iso: str) -> float:
    if not isinstance(start_iso, str) or not isinstance(end_iso, str):
        raise ValueError("Inputs must be strings")
    try:
        dt_start = datetime.fromisoformat(start_iso)
        dt_end = datetime.fromisoformat(end_iso)
    except ValueError as e:
        raise ValueError(f"Invalid ISO 8601 format: {e}")
    if dt_start.tzinfo is None:
        dt_start = dt_start.replace(tzinfo=timezone.utc)
    if dt_end.tzinfo is None:
        dt_end = dt_end.replace(tzinfo=timezone.utc)
    delta = dt_end - dt_start
    return delta.total_seconds()

if __name__ == '__main__':
    t1 = "2024-05-15T10:30:00+00:00"
    t2 = "2024-05-15T12:45:30+00:00"
    diff = compute_seconds_delta(t1, t2)
    print(diff)