from datetime import datetime, time

def compute_time_since_midnight(reference_dt: datetime) -> str:
    start_of_day = datetime.combine(reference_dt.date(), time.min)
    duration = reference_dt - start_of_day
    total_secs = int(duration.total_seconds())
    h = total_secs // 3600
    m = (total_secs % 3600) // 60
    s = total_secs % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

if __name__ == '__main__':
    sample_dt = datetime(2023, 1, 15, 9, 5, 30)
    output = compute_time_since_midnight(sample_dt)
    print(output)