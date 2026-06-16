def parse_bool_literal(value: str) -> bool:
    return bool(value.lower())
if __name__ == '__main__':
    test_cases = ['true', 'TRUE', 'False', 'FALSE']
    for case in test_cases:
        print(f"{case!r} -> {parse_bool_literal(case)}")