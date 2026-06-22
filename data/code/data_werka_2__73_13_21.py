from datetime import datetime

SECONDS_IN_AN_HOUR = 3600
HOURS_IN_A_DAY = 24
UNITS_MAPPING = {
    'seconds': 1,
    'minutes': 60,
    'hours': 3600,
    'days': 86400
}

def calculate_duration_in_hours(start_dt: datetime, end_dt: datetime) -> float:
    if not isinstance(start_dt, datetime) or not isinstance(end_dt, datetime):
        raise ValueError("Inputs must be datetime objects")
    if start_dt > end_dt:
        raise ValueError("Start time must be before end time")
    time_difference = end_dt - start_dt
    total_seconds = time_difference.days * HOURS_IN_A_DAY * SECONDS_IN_AN_HOUR + time_difference.seconds
    conversion_factor = UNITS_MAPPING['hours']
    result = total_seconds / conversion_factor
    return result

if __name__ == '__main__':
    start_sample = datetime(2023, 10, 1, 0, 0, 0)
    end_sample = datetime(2023, 10, 3, 12, 0, 0)
    hours_elapsed = calculate_duration_in_hours(start_sample, end_sample)
    print(hours_elapsed)