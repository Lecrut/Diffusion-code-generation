from datetime import datetime, time

def get_elapsed_time_since_midnight(reference_time: datetime = None) -> tuple:
    if reference_time is None:
        reference_time = datetime.now()
    midnight = reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
    delta_seconds = int((reference_time - midnight).total_seconds())
    if delta_seconds < 0:
        raise ValueError("Reference time must be today or later")
    hours = delta_seconds // 3600
    remainder = delta_seconds % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    sample_dt = datetime(2023, 10, 5, 14, 30, 45)
    h, m, s = get_elapsed_time_since_midnight(sample_dt)
    print(f"{h} hours, {m} minutes, {s} seconds")