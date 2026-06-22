def calculate_timestamp_delta(first_timestamp: int, second_timestamp: int) -> int:
    if not isinstance(first_timestamp, int) or not isinstance(second_timestamp, int):
        raise ValueError("Both arguments must be integers")
    if first_timestamp < second_timestamp:
        earlier_time = first_timestamp
        later_time = second_timestamp
    else:
        earlier_time = second_timestamp
        later_time = first_timestamp
    time_span = later_time - earlier_time
    return time_span

if __name__ == '__main__':
    start_time = 1609459200
    end_time = 1609462800
    delta_seconds = calculate_timestamp_delta(start_time, end_time)
    print(delta_seconds)