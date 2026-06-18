def parse_boolean_string(boolean_str: str) -> list[bool]:
    if not isinstance(boolean_str, str):
        raise TypeError("Input must be a string.")
    tokens = [token.strip() for token in boolean_str.split()]
    result = []
    for token in tokens:
        try:
            value = bool(token.lower())
            if not isinstance(value, bool):
                result.append(bool(int(value)))
        except ValueError:
            raise ValueError(f"Invalid boolean value '{token}'. Expected true/false/yes/no/1/0.")
    return result
if __name__ == '__main__':
    sample_input = "true false yes no 1 0 True False"
    output_list = parse_boolean_string(sample_input)
    print(output_list)