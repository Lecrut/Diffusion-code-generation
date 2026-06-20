from datetime import datetime

def compute_duration(start_time: str, end_time: str) -> float:
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    duration = end - start
    return duration.total_seconds() / 3600

if __name__ == '__main__':
    sample_start = "2023-10-01 08:45:00"
    sample_end = "2023-10-01 10:15:00"
    duration_in_hours = compute_duration(sample_start, sample_end)
    print(f"Duration in hours: {duration_in_hours:.2f}")