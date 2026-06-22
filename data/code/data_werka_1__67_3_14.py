def sum_generator(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers")
    yield a + b

if __name__ == '__main__':
    try:
        sample_a = 7.5
        sample_b = 4.25
        result = next(sum_generator(sample_a, sample_b))
        print(result)
    except ValueError as e:
        print(e)