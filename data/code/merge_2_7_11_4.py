def parse_boolean_string(boolean_str: str) -> list[bool]:
    if not isinstance(boolean_str, str):
        raise TypeError("Input must be a string.")
    tokens = [token.strip() for token in boolean_str.split()]
    result = []
    for token in tokens:
        lower_token = token.lower()
        try:
            if lower_token == "true" or lower_token == "yes":
                result.append(True)
            elif lower_token == "false" or lower_token == "no":
                result.append(False)
            else:
                value = int(token)
                if value not in (0, 1):
                    raise ValueError(f"Invalid boolean representation: '{token}'")
                result.append(bool(value))
        except ValueError:
            raise ValueError(f"Cannot convert '{token}' to boolean.")
    return result
if __name__ == '__main__':
    sample_input = "true false yes no 1 0 invalid True FALSE"
    try:
        output = parse_boolean_string(sample_input)
        print(output)
    except ValueError as e:
        print(f"Error: {e}")