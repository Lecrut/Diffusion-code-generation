def parse_boolean_string(input_str: str) -> list[bool]:
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string.")
    tokens = input_str.strip().split()
    result = []
    for token in tokens:
        try:
            value = bool(token)
            if not isinstance(value, bool):
                raise ValueError(f"Invalid boolean representation: '{token}'")
            result.append(value)
        except Exception as e:
            raise ValueError(f"Failed to parse token '{token}': {e}") from None
    return result
if __name__ == '__main__':
    sample_input = "true false True FALSE 1 0 yes no"
    output_result = parse_boolean_string(sample_input)
    print(output_result)