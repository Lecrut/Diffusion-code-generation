def parse_boolean_string(input_str: str) -> list[bool]:
    try:
        return [val.lower() in ("true", "1") for val in input_str.split()]
    except Exception as e:
        raise TypeError(f"Invalid input format. Expected space-separated true/false or 0/1, got {input_str!r}") from e
if __name__ == '__main__':
    sample_input = "true false True 1 FALSE 0 invalid"
    result = parse_boolean_string(sample_input)
    print(result)