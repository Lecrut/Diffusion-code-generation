from datetime import datetime, time

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def compute_time_since_midnight(reference: datetime) -> str:
    start_of_day = datetime.combine(reference.date(), time.min)
    delta = reference - start_of_day
    total_seconds = int(delta.total_seconds())
    hours = total_seconds // SECONDS_PER_HOUR
    remaining_seconds = total_seconds % SECONDS_PER_HOUR
    minutes = remaining_seconds // SECONDS_PER_MINUTE
    seconds = remaining_seconds % SECONDS_PER_MINUTE
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    now = datetime.now()
    output = compute_time_since_midnight(now)
    print(output)