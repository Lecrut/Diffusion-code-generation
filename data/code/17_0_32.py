def is_even(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [10, -5, 3, 8, 0, -7]
    results = {value: is_even(value) for value in sample_values}
    print(results)