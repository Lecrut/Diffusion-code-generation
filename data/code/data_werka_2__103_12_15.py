from datetime import datetime, timedelta

def calculate_elapsed_since_midnight(reference_time: datetime) -> dict:
    if reference_time.tzinfo is not None:
        reference_time = reference_time.replace(tzinfo=None)
    start_of_day = reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = reference_time - start_of_day
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // 3600
    remainder = total_seconds % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return {"hours": hours, "minutes": minutes, "seconds": seconds}

if __name__ == '__main__':
    sample_time = datetime(2023, 10, 27, 15, 45, 30)
    result = calculate_elapsed_since_midnight(sample_time)
    print(f"{result['hours']} hours, {result['minutes']} minutes, {result['seconds']} seconds")