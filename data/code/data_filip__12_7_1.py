import re

def clean_and_verify_integers(raw: str) -> str:
    trans_table = str.maketrans('', '', ' \t\n\r\v\f.,;:!@#$%^&*()_+-=[]{}|\'"\\/<>?~`')
    cleaned = raw.translate(trans_table)
    if not cleaned:
        raise ValueError("Empty string after cleaning")
    parts = cleaned.split('-')
    if len(parts) > 1:
        first_part = parts[0]
        if not first_part:
            negative_rest = '-'.join(parts[1:])
            if not negative_rest:
                raise ValueError("Invalid integer: '-'")
            if not negative_rest.isdigit():
                raise ValueError(f"Invalid integer: {cleaned}")
            return '-' + negative_rest
        if first_part:
            raise ValueError(f"Invalid integer: {cleaned}")
    if not cleaned.isdigit():
        raise ValueError(f"Invalid integer: {cleaned}")
    return cleaned

if __name__ == '__main__':
    test_input = "  123.45  "
    try:
        result = clean_and_verify_integers(test_input)
        print(result)
    except ValueError as e:
        print(e)
    test_input_neg = " -987 "
    try:
        result_neg = clean_and_verify_integers(test_input_neg)
        print(result_neg)
    except ValueError as e:
        print(e)