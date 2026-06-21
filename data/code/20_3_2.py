def is_divisible_by_two(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [4, 7, -2, 0, 999]
    for val in test_values:
        result = is_divisible_by_two(val)
        print(result)