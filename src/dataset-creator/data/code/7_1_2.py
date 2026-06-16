def parse_boolean_literal(value: str) -> bool:
    return bool(value.lower() in ('true', 'false'))
if __name__ == '__main__':
    test_cases = ['True', 'FALSE', 'TRUE', 'False']
    for case in test_cases:
        result = parse_boolean_literal(case)
        print(f"{case!r} -> {result}")