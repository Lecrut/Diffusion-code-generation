from datetime import datetime, time, timedelta

def format_elapsed_since_midnight(reference_time: datetime) -> str:
    if not isinstance(reference_time, datetime):
        raise ValueError("reference_time must be a datetime instance")
    if reference_time.tzinfo is not None:
        raise ValueError("reference_time must be naive (no timezone)")
    midnight = datetime.combine(reference_time.date(), time.min)
    delta = reference_time - midnight
    total_seconds = int(delta.total_seconds())
    if total_seconds < 0 or total_seconds >= 86400:
        raise ValueError("reference_time must be within the same day as midnight")
    hours = total_seconds // 3600
    remainder = total_seconds % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    sample_time = datetime(2023, 10, 27, 14, 30, 45)
    output = format_elapsed_since_midnight(sample_time)
    print(output)