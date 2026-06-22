def is_even(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [15, -4, 7, 0, 3, -8, 11, 6]
    results = {value: is_even(value) for value in sample_values}
    print(results)