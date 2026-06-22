from datetime import datetime, timezone

def compute_time_delta_in_hours(reference_time: datetime, comparison_time: datetime) -> float:
    if reference_time.tzinfo is None:
        raise ValueError("Reference time must be timezone-aware")
    if comparison_time.tzinfo is None:
        raise ValueError("Comparison time must be timezone-aware")
    
    normalized_reference = reference_time.astimezone(timezone.utc)
    normalized_comparison = comparison_time.astimezone(timezone.utc)
    
    time_difference = normalized_comparison - normalized_reference
    raw_seconds = time_difference.total_seconds()
    hours_result = raw_seconds / 3600.0
    return hours_result

if __name__ == '__main__':
    base_tz = timezone.utc
    start_dt = datetime(2023, 5, 10, 14, 30, 0, tzinfo=base_tz)
    end_dt = datetime(2023, 5, 10, 17, 45, 0, tzinfo=base_tz)
    delta_hours = compute_time_delta_in_hours(start_dt, end_dt)
    print(delta_hours)