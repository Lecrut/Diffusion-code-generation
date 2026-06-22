def compute_time_delta_hours(t1, t2):
    if not isinstance(t1, (int, float)):
        raise ValueError("First timestamp must be numeric")
    if not isinstance(t2, (int, float)):
        raise ValueError("Second timestamp must be numeric")
    return (t2 - t1) / 3600.0

if __name__ == '__main__':
    t_start = 1609459200
    t_end = 1609462800
    print(compute_time_delta_hours(t_start, t_end))