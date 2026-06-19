def is_even(n):
    return (n & 1) == 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, -3, 4, -5, 6, -7, 8, -9]
    results = {value: is_even(value) for value in sample_values}
    print(results)