def is_divisible_by_two(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    test_values = [2, 3, 4, 5, 10, -5, -4]
    for n in test_values:
        result = is_divisible_by_two(n)
        print(result)