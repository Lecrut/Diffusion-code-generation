def is_positive(value: int | float) -> bool:
    return value > 0
if __name__ == '__main__':
    test_cases = [1, -5, 3.14, 0, 2]
    for case in test_cases:
        result = is_positive(case)
        print(f"is_positive({case}) = {result}")