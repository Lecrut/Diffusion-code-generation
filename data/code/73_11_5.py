SECONDS_PER_HOUR = 3600

def calculate_time_difference_hours(start_ts, end_ts):
    if not isinstance(start_ts, (int, float)):
        raise ValueError("start_ts must be numeric")
    if not isinstance(end_ts, (int, float)):
        raise ValueError("end_ts must be numeric")
    raw_difference = end_ts - start_ts
    hours = raw_difference / SECONDS_PER_HOUR
    return hours

if __name__ == '__main__':
    t_start = 1700000000
    t_end = 1700003600
    diff_hours = calculate_time_difference_hours(t_start, t_end)
    print(diff_hours)