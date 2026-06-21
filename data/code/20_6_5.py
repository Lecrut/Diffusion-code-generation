def is_even(n: int) -> bool:
    return (n & 1) == 0

if __name__ == '__main__':
    values = [0, 1, 2, 3, 10, 11, -4, -5]
    results = [is_even(v) for v in values]
    print(results)