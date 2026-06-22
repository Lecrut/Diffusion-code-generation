def is_valid_number(value):
    return isinstance(value, (int, float))

def sum_generator(a, b):
    if not is_valid_number(a) or not is_valid_number(b):
        raise ValueError("Both arguments must be numbers")
    yield a + b

if __name__ == '__main__':
    sample_a = 7
    sample_b = 3.5
    result = next(sum_generator(sample_a, sample_b))
    print(result)