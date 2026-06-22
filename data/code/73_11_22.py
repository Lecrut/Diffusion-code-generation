def compute_time_delta_hours(first_ts, second_ts):
    if not isinstance(first_ts, (int, float)):
        raise ValueError("first_ts must be a number")
    if not isinstance(second_ts, (int, float)):
        raise ValueError("second_ts must be a number")
    unit_mapping = {
        "seconds": 1.0,
        "minutes": 60.0,
        "hours": 3600.0,
        "days": 86400.0
    }
    target_unit = "hours"
    conversion_factor = unit_mapping[target_unit]
    delta_seconds = second_ts - first_ts
    delta_hours = delta_seconds / conversion_factor
    return delta_hours

if __name__ == '__main__':
    t1 = 1700000000
    t2 = 1700003600
    output = compute_time_delta_hours(t1, t2)
    print(output)