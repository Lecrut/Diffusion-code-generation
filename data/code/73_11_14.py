from datetime import datetime

CONVERSION_UNITS = {
    "seconds": 1,
    "minutes": 60,
    "hours": 3600,
    "days": 86400
}

def get_time_difference_hours(timestamp_a, timestamp_b):
    if not isinstance(timestamp_a, (int, float)):
        raise ValueError("timestamp_a must be a numeric value")
    if not isinstance(timestamp_b, (int, float)):
        raise ValueError("timestamp_b must be a numeric value")
    
    seconds_diff = abs(timestamp_a - timestamp_b)
    hours_diff = seconds_diff / CONVERSION_UNITS["hours"]
    return hours_diff

if __name__ == '__main__':
    ts_start = 1672531200
    ts_end = 1672534800
    output = get_time_difference_hours(ts_start, ts_end)
    print(output)