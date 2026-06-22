from datetime import datetime, time

def format_elapsed_time_since_midnight(reference_datetime: datetime) -> str:
    if not isinstance(reference_datetime, datetime):
        raise ValueError("reference_datetime must be a datetime instance")
    if reference_datetime.tzinfo is not None:
        raise ValueError("reference_datetime must be naive (no timezone)")
    if not (0 <= reference_datetime.hour < 24 and
            0 <= reference_datetime.minute < 60 and
            0 <= reference_datetime.second < 60):
        raise ValueError("reference_datetime components must be valid time values")
    midnight = datetime.combine(reference_datetime.date(), time.min)
    delta = reference_datetime - midnight
    total_seconds = int(delta.total_seconds())
    if not (0 <= total_seconds < 86400):
        raise ValueError("reference_datetime must be within the same day as midnight")
    hours = total_seconds // 3600
    remainder = total_seconds % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    sample_time = datetime(2023, 10, 27, 14, 30, 45)
    result = format_elapsed_time_since_midnight(sample_time)
    print(result)