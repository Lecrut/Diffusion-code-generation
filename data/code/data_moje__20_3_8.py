def is_divisible_by_two(n):
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 4, 5, -2, -3, -4]
    results = [is_divisible_by_two(val) for val in sample_values]
    print(results)