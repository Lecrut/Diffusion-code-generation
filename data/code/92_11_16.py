def reverse_boolean_literal(text: str) -> str:
    def validate_and_parse(val: str):
        if val is None:
            raise ValueError("Input cannot be None")
        cleaned = val.strip()
        if not cleaned:
            raise ValueError("Input string cannot be empty")
        lower_cleaned = cleaned.lower()
        if lower_cleaned == 'true':
            return True
        if lower_cleaned == 'false':
            return False
        raise ValueError(f"Unknown boolean literal: {cleaned}")

    is_true = validate_and_parse(text)
    result_value = not is_true
    return str(result_value)

if __name__ == '__main__':
    print(reverse_boolean_literal('True'))
    print(reverse_boolean_literal('False'))
    print(reverse_boolean_literal('TRUE'))
    print(reverse_boolean_literal('false'))
    print(reverse_boolean_literal(' TrUe '))
    print(reverse_boolean_literal('FaLsE'))