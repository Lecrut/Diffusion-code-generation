def is_divisible_by_two(n: int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return n % 2 == 0

if __name__ == '__main__':
    result = is_divisible_by_two(4)
    print(result)
    result = is_divisible_by_two(7)
    print(result)
    result = is_divisible_by_two(0)
    print(result)