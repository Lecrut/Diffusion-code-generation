def is_odd(n: int) -> bool:
    return (n & 1) != 0
if __name__ == '__main__':
    test_cases = [42, -5, 0, 1]
    for val in test_cases:
        result = "Odd" if is_odd(val) else "Even"
        print(f"{val} is {result}")