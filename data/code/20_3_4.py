def is_divisible_by_two(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    values = [-4, -3, 0, 1, 2, 100, 101]
    for v in values:
        print(is_divisible_by_two(v))