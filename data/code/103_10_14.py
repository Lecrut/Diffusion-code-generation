from datetime import datetime, timedelta

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60
HOURS_IN_DAY = 24

TIME_UNITS = {
    "hours": SECONDS_PER_HOUR,
    "minutes": SECONDS_PER_MINUTE,
    "seconds": 1
}

def calculate_elapsed_since_day_start(reference_date: datetime) -> dict:
    if not isinstance(reference_date, datetime):
        raise ValueError("reference_date must be a datetime object")
    
    start_of_day = reference_date.replace(hour=0, minute=0, second=0, microsecond=0)
    
    delta = reference_date - start_of_day
    total_seconds = int(delta.total_seconds())
    
    if total_seconds < 0:
        raise ValueError("reference_date cannot be before start_of_day")
        
    hours = total_seconds // SECONDS_PER_HOUR
    remaining_seconds = total_seconds % SECONDS_PER_HOUR
    minutes = remaining_seconds // SECONDS_PER_MINUTE
    seconds = remaining_seconds % SECONDS_PER_MINUTE
    
    return {
        "total_seconds": total_seconds,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "formatted": f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    }

def get_time_component(total_seconds: int, unit_key: str) -> int:
    if unit_key not in TIME_UNITS:
        raise ValueError(f"Unsupported unit: {unit_key}")
    
    unit_seconds = TIME_UNITS[unit_key]
    return total_seconds // unit_seconds

if __name__ == '__main__':
    sample_date = datetime(2024, 1, 15, 13, 45, 30)
    
    result = calculate_elapsed_since_day_start(sample_date)
    
    print(result["formatted"])
    print(result["total_seconds"])
    print(result["hours"])
    
    component_hours = get_time_component(result["total_seconds"], "hours")
    print(component_hours)