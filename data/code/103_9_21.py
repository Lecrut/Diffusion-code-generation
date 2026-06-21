from datetime import datetime, time, timedelta

def compute_elapsed_since_midnight(reference: datetime) -> str:
    if not isinstance(reference, datetime):
        raise ValueError("reference must be a datetime instance")
    if reference.tzinfo is not None:
        raise ValueError("reference must be naive")
    midnight = datetime.combine(reference.date(), time.min)
    delta = reference - midnight
    total_seconds = int(delta.total_seconds())
    if total_seconds < 0 or total_seconds >= 86400:
        raise ValueError("reference must be within the same day")
    hours = total_seconds // 3600
    remainder = total_seconds % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    sample_time = datetime(2023, 10, 27, 14, 30, 45)
    result = compute_elapsed_since_midnight(sample_time)
    print(result)