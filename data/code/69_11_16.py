def access_string_characters(text, positions):
    result = []
    for pos in positions:
        if 0 <= pos < len(text):
            result.append(text[pos])
        else:
            result.append(None)
    return result

if __name__ == '__main__':
    sample_text = "Hello, World!"
    sample_positions_valid = [0, 7, 12]
    sample_positions_invalid = [-1, 15, 3]
    result_valid = access_string_characters(sample_text, sample_positions_valid)
    print(f"Text: {sample_text}")
    print(f"Positions (Valid): {sample_positions_valid}")
    print(f"Result (Valid): {result_valid}")
    result_invalid = access_string_characters(sample_text, sample_positions_invalid)
    print(f"Positions (Invalid): {sample_positions_invalid}")
    print(f"Result (Invalid): {result_invalid}")