def access_string_characters(s, indices):
    result = []
    for index in indices:
        if 0 <= index < len(s):
            result.append(s[index])
        else:
            result.append(None)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices_valid = [0, 7, 12]
    sample_indices_invalid = [-5, 13, 8]
    
    valid_characters = access_string_characters(sample_string, sample_indices_valid)
    print(f"String: {sample_string}")
    print(f"Valid Indices: {sample_indices_valid}")
    print(f"Result (Valid): {valid_characters}")
    
    invalid_characters = access_string_characters(sample_string, sample_indices_invalid)
    print(f"Invalid Indices: {sample_indices_invalid}")
    print(f"Result (Invalid): {invalid_characters}")