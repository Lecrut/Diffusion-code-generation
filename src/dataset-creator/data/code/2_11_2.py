def is_positive(value: int | float) -> bool:
    return value > 0
if __name__ == '__main__':
    test_cases = [1, -2, 0.0, 0.5, float('inf'), None]
    for case in test_cases:
        try:
            result = is_positive(case) if isinstance(case, (int, float)) else "Invalid type"
            print(f"is_positive({case!r}) -> {result}")
        except Exception as e:
            print(f"is_positive({case!r}) raised an error")