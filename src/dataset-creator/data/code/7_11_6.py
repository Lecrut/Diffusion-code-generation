def parse_boolean_string(input_str: str) -> list[bool]:
    result = []
    for token in input_str.strip().split():
        if not isinstance(token, str):
            raise TypeError(f"Expected string tokens, got {type(token).__name__}")
        try:
            normalized = token.lower()
            result.append(normalized == "true")
            if not (normalized in ("true", "false")):
                raise ValueError(f"Invalid boolean value '{token}'")
        except Exception as e:
            raise TypeError(f"Error parsing input string: {e}") from None
    return result
if __name__ == '__main__':
    sample_input = "True False TRUE false True invalid 1"
    try:
        output = parse_boolean_string(sample_input)
        print(output if isinstance(output, list) else f"[{output}]")
    except Exception as e:
        print(f"Error occurred: {e}")