from datetime import datetime, timedelta

def get_elapsed_time_since_midnight(reference_time: datetime) -> dict:
    midnight = reference_time.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = reference_time - midnight
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return {
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }

if __name__ == '__main__':
    sample_time = datetime(2023, 10, 5, 14, 30, 45)
    result = get_elapsed_time_since_midnight(sample_time)
    print(result)