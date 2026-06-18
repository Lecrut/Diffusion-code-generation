def is_negative(n: int) -> bool:
    return n < 0

if __name__ == '__main__':
    test_cases = [-5, -1, 0, 1, 42]
    for val in test_cases:
        result = is_negative(val)
        print(f"is_negative({val}) = {result}")