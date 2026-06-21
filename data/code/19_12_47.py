def is_even(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [15, -24, 7, 8, 0, -1]
    results = {value: is_even(value) for value in sample_values}
    print(results)