def is_divisible_by_two(n: int) -> bool:
    if n < 0:
        n = -n
    return (n & 1) == 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, 10, -3, 42]
    results = [is_divisible_by_two(val) for val in sample_values]
    print(results)