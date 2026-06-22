def calculate_seconds_between(ts_first: int, ts_second: int) -> int:
    if type(ts_first) is not int or type(ts_second) is not int:
        raise ValueError("Arguments must be integers")
    difference = ts_first - ts_second
    if difference < 0:
        return -difference
    return difference

if __name__ == '__main__':
    time_a = 1672531200
    time_b = 1672531260
    output = calculate_seconds_between(time_a, time_b)
    print(output)