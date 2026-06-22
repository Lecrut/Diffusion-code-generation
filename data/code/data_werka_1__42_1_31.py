def build_string_from_parts(parts):
    if not isinstance(parts, list):
        raise ValueError("Input must be a list of strings.")
    if not all(isinstance(part, str) for part in parts):
        raise ValueError("All elements in the list must be strings.")
    
    return ' '.join(parts)

if __name__ == '__main__':
    sample_parts = ["hello", "world", "from", "python"]
    try:
        output = build_string_from_parts(sample_parts)
        print(output)
    except ValueError as e:
        print(e)

    invalid_input_1 = [1, 2, 3]
    try:
        output = build_string_from_parts(invalid_input_1)
        print(output)
    except ValueError as e:
        print(e)

    invalid_input_2 = "not a list"
    try:
        output = build_string_from_parts(invalid_input_2)
        print(output)
    except ValueError as e:
        print(e)