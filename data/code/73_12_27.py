from datetime import datetime, timezone

def calculate_time_difference_seconds(ts_a: str, ts_b: str) -> float:
    def parse_iso_timestamp(ts: str) -> datetime:
        if not isinstance(ts, str):
            raise ValueError("Timestamp must be a string")
        try:
            dt = datetime.fromisoformat(ts)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError as e:
            raise ValueError(f"Invalid ISO 8601 timestamp: {ts}") from e

    dt_a = parse_iso_timestamp(ts_a)
    dt_b = parse_iso_timestamp(ts_b)
    
    delta = dt_b - dt_a
    return delta.total_seconds()

if __name__ == '__main__':
    start_time = "2023-06-15T08:30:00Z"
    end_time = "2023-06-15T09:45:30Z"
    diff = calculate_time_difference_seconds(start_time, end_time)
    print(diff)