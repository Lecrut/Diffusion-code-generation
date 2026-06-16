def parse_boolean_literal(value: str) -> bool:
    return bool(str(value).lower())
if __name__ == '__main__':
    test_cases = ['true', 'false', 'True', 'FALSE']
    for case in test_cases:
        result = parse_boolean_literal(case)
        print(f"{case!r} -> {result}")