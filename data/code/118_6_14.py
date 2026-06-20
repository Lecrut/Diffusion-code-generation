def validate_inputs(a, b):
    if not all(isinstance(i, (int, float)) for i in [a, b]):
        raise ValueError("Both inputs must be numbers")

product = lambda x, y: x * y

if __name__ == '__main__':
    sample_a = 3
    sample_b = 4
    validate_inputs(sample_a, sample_b)
    result = product(sample_a, sample_b)
    print(result)