HOURS_PER_DAY = 24
SECONDS_PER_HOUR = 60
MINUTES_PER_HOUR = 60
SECONDS_PER_DAY = HOURS_PER_DAY * SECONDS_PER_HOUR

def get_time_difference_hours(point_a, point_b):
    if not isinstance(point_a, (int, float)):
        raise ValueError("point_a must be numeric")
    if not isinstance(point_b, (int, float)):
        raise ValueError("point_b must be numeric")
    
    delta_seconds = point_b - point_a
    delta_hours = delta_seconds / SECONDS_PER_HOUR
    return delta_hours

if __name__ == '__main__':
    ts_start = 1609459200
    ts_end = 1609462800
    output = get_time_difference_hours(ts_start, ts_end)
    print(output)