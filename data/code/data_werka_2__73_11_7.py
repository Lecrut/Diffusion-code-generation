def time_difference_in_hours(start_timestamp, end_timestamp):
    if not isinstance(start_timestamp, (int, float)):
        raise ValueError("start_timestamp must be a number")
    if not isinstance(end_timestamp, (int, float)):
        raise ValueError("end_timestamp must be a number")
    difference_seconds = end_timestamp - start_timestamp
    difference_hours = difference_seconds / 3600.0
    return difference_hours

if __name__ == '__main__':
    start = 1609459200.0
    end = 1609462800.0
    result = time_difference_in_hours(start, end)
    print(result)