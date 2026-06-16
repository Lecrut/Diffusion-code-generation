def is_odd(n: int) -> bool:
    return (n & 1) != 0
if __name__ == '__main__':
    test_cases = [5, -3, 42, -7]
    for val in test_cases:
        result = "Odd" if is_odd(val) else "Even"
        print(f"{val}: {result}")