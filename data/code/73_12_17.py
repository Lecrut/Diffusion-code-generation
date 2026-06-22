from datetime import datetime, timezone
import time

ISO_8601_BASE_FMT = "%Y-%m-%dT%H:%M:%S"

def parse_iso_timestamp(ts: str) -> datetime:
    if not isinstance(ts, str):
        raise ValueError("Input must be a string")
    if len(ts) < 19:
        raise ValueError("Timestamp string too short")
    try:
        dt = datetime.strptime(ts, ISO_8601_BASE_FMT)
    except ValueError as e:
        raise ValueError(f"Invalid ISO 8601 format: {ts}") from e
    return dt.replace(tzinfo=timezone.utc)

def compute_seconds_difference(start_ts: str, end_ts: str) -> float:
    dt_start = parse_iso_timestamp(start_ts)
    dt_end = parse_iso_timestamp(end_ts)
    delta_seconds = (dt_end - dt_start).total_seconds()
    return delta_seconds

if __name__ == '__main__':
    sample_start = "2024-01-01T00:00:00"
    sample_end = "2024-01-01T01:00:00"
    diff = compute_seconds_difference(sample_start, sample_end)
    print(diff)