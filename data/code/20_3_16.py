def is_divisible_by_two(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 4, 5, -1, -2, 100, 99]
    for value in sample_values:
        result = is_divisible_by_two(value)
        print(f"{value}: {result}")