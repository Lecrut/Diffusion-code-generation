def is_even(n: int) -> bool:
    return (n & 1) == 0

if __name__ == '__main__':
    values = [4, 7, 0, -3, 100]
    for v in values:
        print(is_even(v))