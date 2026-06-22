SECOND_TIMESTAMP_UNITS = 1

def calculate_timestamp_span(first: int, second: int) -> int:
    if not isinstance(first, int) or not isinstance(second, int):
        raise ValueError("Timestamps must be integers")
    span = second - first
    return span * SECOND_TIMESTAMP_UNITS if span >= 0 else span * -1

if __name__ == '__main__':
    t_one = 1672531200
    t_two = 1672531260
    difference = calculate_timestamp_span(t_one, t_two)
    print(difference)