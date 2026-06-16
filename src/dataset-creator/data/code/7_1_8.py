def parse_boolean(value: str) -> bool:
    return bool(str.lower(value))
if __name__ == '__main__':
    test_cases = ['true', 'false', 'True', 'FALSE']
    for case in test_cases:
        print(f"{case!r} -> {parse_boolean(case)}")