def add_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError('Both inputs must be integers')
    return a + b
if __name__ == '__main__':
    sample_a = 10
    sample_b = 20
    result = add_numbers(sample_a, sample_b)
    print(f'The sum of {sample_a} and {sample_b} is: {result}')