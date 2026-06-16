def parse_boolean_literal(value: str) -> bool:
    return bool(value.lower() in ('true', 'false'))
if __name__ == '__main__':
    sample_values = ['true', 'False', 'FALSE', 'TRUE']
    for val in sample_values:
        result = parse_boolean_literal(val)
        print(f"{val!r} -> {result}")