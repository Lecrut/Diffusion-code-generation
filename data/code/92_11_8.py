def reverse_boolean_literal(text: str) -> str:
    trimmed = text.strip()
    normalized = trimmed.lower()
    if normalized in ('true', 't', '1', 'yes'):
        return 'False'
    if normalized in ('false', 'f', '0', 'no'):
        return 'True'
    raise ValueError(f"Invalid boolean literal: {trimmed}")

if __name__ == '__main__':
    test_input = 'YES'
    result = reverse_boolean_literal(test_input)
    print(result)
    test_input = '0'
    result = reverse_boolean_literal(test_input)
    print(result)