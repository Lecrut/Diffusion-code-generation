def extract_chars_from_string(s, indices):
    result = []
    for index in indices:
        if 0 <= index < len(s):
            result.append(s[index])
        else:
            result.append(None)
    return result

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices_valid = [0, 7, 12]
    sample_indices_invalid = [13, -1, 5]
    valid_result = extract_chars_from_string(sample_string, sample_indices_valid)
    print(f"String: {sample_string}")
    print(f"Indices (Valid): {sample_indices_valid}")
    print(f"Result (Valid): {valid_result}")
    invalid_result = extract_chars_from_string(sample_string, sample_indices_invalid)
    print(f"Indices (Invalid): {sample_indices_invalid}")
    print(f"Result (Invalid): {invalid_result}")