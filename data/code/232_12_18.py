def print_incrementing_sequence(start=0):
    if not isinstance(start, (int, float)):
        raise ValueError("Start value must be an integer or float")

    current_value = start
    step_size = 1

    for _ in range(5):
        print(current_value)
        current_value += step_size
        step_size += 1

if __name__ == '__main__':
    try:
        print_incrementing_sequence()
    except ValueError as e:
        print(e)