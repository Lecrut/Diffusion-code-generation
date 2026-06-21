def validate_indices(data_length, indices):
    return [index for index in indices if 0 <= index < data_length]

def access_string_elements(s, indices):
    valid_indices = validate_indices(len(s), indices)
    return ''.join(s[index] for index in valid_indices)

if __name__ == '__main__':
    sample_string = "HelloWorld"
    sample_indices_valid = [0, 4, 7]
    sample_indices_invalid = [10, -2, 5]

    result_valid = access_string_elements(sample_string, sample_indices_valid)
    print(f"Sample String: {sample_string}")
    print(f"Valid Indices: {sample_indices_valid}")
    print(f"Result (Valid): {result_valid}")

    result_invalid = access_string_elements(sample_string, sample_indices_invalid)
    print(f"Invalid Indices: {sample_indices_invalid}")