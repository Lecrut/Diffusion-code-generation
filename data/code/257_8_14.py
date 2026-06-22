def calculate_difference(time1, time2):
    if not (isinstance(time1, tuple) and isinstance(time2, tuple)):
        raise ValueError('Both inputs must be tuples.')
    if len(time1) != 3 or len(time2) != 3:
        raise ValueError('Tuples must contain exactly three elements: hours, minutes, seconds.')
    for t in [time1, time2]:
        if not all((isinstance(x, int) and x >= 0 for x in t)):
            raise ValueError('All elements in the tuples must be non-negative integers.')
    total_seconds_time1 = time1[0] * 3600 + time1[1] * 60 + time1[2]
    total_seconds_time2 = time2[0] * 3600 + time2[1] * 60 + time2[2]
    return abs(total_seconds_time1 - total_seconds_time2)
if __name__ == '__main__':
    sample_time1 = (1, 30, 45)
    sample_time2 = (1, 45, 30)
    print(calculate_difference(sample_time1, sample_time2))