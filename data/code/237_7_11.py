def validate_start_value(start_value):
    if not isinstance(start_value, int) or start_value < 0:
        raise ValueError("Start value must be a non-negative integer")

def generate_even_numbers(start_value, count):
    return [start_value + 2 * i for i in range(count)]

if __name__ == '__main__':
    start = 2
    count = 10
    validate_start_value(start)
    result = generate_even_numbers(start, count)
    print(result)