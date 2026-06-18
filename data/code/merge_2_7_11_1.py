def parse_boolean_string(boolean_str: str) -> list[bool]:
    if not boolean_str.strip():
        return []
    try:
        values = [token.lower().strip() for token in boolean_str.split()]
        result = []
        for value in values:
            if value == 'true':
                result.append(True)
            elif value == 'false' or value == '0':
                result.append(False)
            else:
                raise ValueError(f"Invalid boolean value '{value}'")
        return result
    except Exception as e:
        print(f"Error parsing input: {e}")
        return []
if __name__ == '__main__':
    sample_input = "true false True FALSE 0 yes no invalid"
    output = parse_boolean_string(sample_input)
    if not isinstance(output, list):
        print("Output is empty or an error occurred.")
    else:
        for i, val in enumerate(output):
            print(f"{i}: {val}")