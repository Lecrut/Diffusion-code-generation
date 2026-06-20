def access_string_characters(text, positions):
    if not isinstance(text, str) or not all(isinstance(pos, int) for pos in positions):
        raise ValueError("Invalid input: text must be a string and positions must be a list of integers.")
    
    result = []
    for position in positions:
        try:
            result.append(text[position])
        except IndexError:
            result.append(None)
    
    return result

if __name__ == '__main__':
    sample_text = "Hello, World!"
    sample_positions_valid = [0, 4, 7, 11]
    sample_positions_invalid = [-1, 13, 20]
    
    valid_result = access_string_characters(sample_text, sample_positions_valid)
    print(f"Text: {sample_text}")
    print(f"Positions (Valid): {sample_positions_valid}")
    print(f"Result (Valid Positions): {valid_result}")
    
    invalid_result = access_string_characters(sample_text, sample_positions_invalid)
    print(f"Positions (Invalid): {sample_positions_invalid}")
    print(f"Result (Invalid Positions): {invalid_result}")