def parse_boolean_literal(value: str) -> bool:
    return bool(value.lower()) if value in ('true', 'false') else False
if __name__ == '__main__':
    test_cases = ['true', 'FALSE', 'True']
    for case in test_cases:
        print(f"{case!r} -> {parse_boolean_literal(case)}")