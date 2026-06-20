def extract_chars_from_string(input_str, positions):
    result = []
    for pos in positions:
        if 0 <= pos < len(input_str):
            result.append(input_str[pos])
        else:
            result.append(None)
    return result

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_positions_valid = [0, 7, 12]
    sample_positions_invalid = [13, -1, 5]
    valid_chars = extract_chars_from_string(sample_string, sample_positions_valid)
    print(f"String: {sample_string}")
    print(f"Positions (Valid): {sample_positions_valid}")
    print(f"Extracted Chars (Valid): {valid_chars}")
    invalid_chars = extract_chars_from_string(sample_string, sample_positions_invalid)
    print(f"Positions (Invalid): {sample_positions_invalid}")
    print(f"Extracted Chars (Invalid): {invalid_chars}")