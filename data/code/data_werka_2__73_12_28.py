from datetime import datetime, timezone

UNIT_MULTIPLIERS = {
    "seconds": 1,
    "minutes": 60,
    "hours": 3600,
    "days": 86400,
}

def parse_iso_timestamp(ts: str) -> datetime:
    if ts.endswith("Z"):
        ts = ts[:-1] + "+00:00"
    return datetime.fromisoformat(ts)

def compute_difference_seconds(ts1: str, ts2: str) -> float:
    dt1 = parse_iso_timestamp(ts1)
    dt2 = parse_iso_timestamp(ts2)
    delta = dt2 - dt1
    return delta.total_seconds()

if __name__ == '__main__':
    t_start = "2023-01-01T00:00:00Z"
    t_end = "2023-01-01T01:30:45Z"
    diff = compute_difference_seconds(t_start, t_end)
    print(diff)