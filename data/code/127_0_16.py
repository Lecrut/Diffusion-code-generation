def is_odd(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n & 1 == 1

if __name__ == '__main__':
    sample_value = 25
    result = is_odd(sample_value)
    print(result)