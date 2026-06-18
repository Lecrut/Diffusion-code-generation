def parse_boolean_string(input_str: str) -> list[bool]:
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string.")
    result = []
    for token in input_str.split():
        token_lower = token.lower()
        try:
            if token_lower == "true" or token_lower == "1":
                result.append(True)
            elif token_lower == "false" or token_lower == "0":
                result.append(False)
            else:
                raise ValueError(f"Invalid boolean value encountered: '{token}'")
        except Exception as e:
            raise RuntimeError(f"Failed to convert token '{token}': {e}") from None
    return result
if __name__ == '__main__':
    sample_input = "True False yes no 1 TRUE FALSE invalid_value 0"
    try:
        output_list = parse_boolean_string(sample_input)
        print(f"Parsed values: {[str(val).lower() for val in output_list]}")
    except Exception as ex:
        print(f"Error occurred during parsing: {ex}")