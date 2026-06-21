def access_string_characters(s, indices):
    result = []
    for index in indices:
        if 0 <= index < len(s):
            result.append(s[index])
        else:
            result.append(None)
    return result

if __name__ == '__main__':
    sample_string = "HelloWorld"
    sample_indices_valid = [0, 4, 7]
    sample_indices_invalid = [-1, 10, 5]
    
    valid_characters = access_string_characters(sample_string, sample_indices_valid)
    invalid_characters = access_string_characters(sample_string, sample_indices_invalid)
    
    print(f"String: {sample_string}")
    print(f"Valid Indices: {sample_indices_valid}")
    print(f"Characters at Valid Indices: {valid_characters}")
    print(f"Invalid Indices: {sample_indices_invalid}")
    print(f"Characters at Invalid Indices: {invalid_characters}")