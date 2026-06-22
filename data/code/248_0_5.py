def add_two_integers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers")
    return a + b

if __name__ == '__main__':
    sample_a = 10
    sample_b = 20
    result = add_two_integers(sample_a, sample_b)
    print(result)