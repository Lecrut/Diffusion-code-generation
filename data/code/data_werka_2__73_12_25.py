from datetime import datetime, timezone

def calculate_time_difference_in_seconds(ts_a: str, ts_b: str) -> float:
    if not ts_a or not ts_b:
        raise ValueError("Timestamps cannot be empty")
    
    dt_a = datetime.fromisoformat(ts_a)
    dt_b = datetime.fromisoformat(ts_b)
    
    if dt_a.tzinfo is None:
        dt_a = dt_a.replace(tzinfo=timezone.utc)
    if dt_b.tzinfo is None:
        dt_b = dt_b.replace(tzinfo=timezone.utc)
        
    delta = dt_b - dt_a
    return delta.total_seconds()

if __name__ == '__main__':
    start_time = "2023-06-15T10:30:00+00:00"
    end_time = "2023-06-15T12:45:30+00:00"
    diff = calculate_time_difference_in_seconds(start_time, end_time)
    print(diff)