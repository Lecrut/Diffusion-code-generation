def parse_boolean_literal(value: str) -> bool:
    return bool(value.lower() in ('true', 'false'))
if __name__ == '__main__':
    samples = ['true', 'FALSE', 'False']
    for sample in samples:
        result = parse_boolean_literal(sample)
        print(f"{sample!r} -> {result}")