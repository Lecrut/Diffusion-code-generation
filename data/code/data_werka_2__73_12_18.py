from datetime import datetime

UNIT_MULTIPLIERS = {
    'second': 1,
    'minute': 60,
    'hour': 3600,
    'day': 86400
}

def compute_delta_seconds(timestamp_a: str, timestamp_b: str) -> float:
    dt_a = datetime.fromisoformat(timestamp_a)
    dt_b = datetime.fromisoformat(timestamp_b)
    raw_delta = dt_b - dt_a
    return raw_delta.total_seconds()

def get_seconds_from_delta(delta_seconds: float) -> float:
    return delta_seconds * UNIT_MULTIPLIERS['second']

if __name__ == '__main__':
    start_time = "2024-01-01T10:00:00"
    end_time = "2024-01-02T14:30:00"
    raw_seconds = compute_delta_seconds(start_time, end_time)
    final_result = get_seconds_from_delta(raw_seconds)
    print(final_result)