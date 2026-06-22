def is_divisible_by_two(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    print(is_divisible_by_two(4))
    print(is_divisible_by_two(7))
    print(is_divisible_by_two(0))
    print(is_divisible_by_two(-3))
    print(is_divisible_by_two(-8))