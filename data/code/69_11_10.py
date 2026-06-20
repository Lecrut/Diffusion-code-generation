def access_string_chars_by_indices(input_str, indices):
    result = []
    max_index = len(input_str) - 1
    for index in indices:
        if 0 <= index <= max_index:
            result.append(f"Character at index {index}: '{input_str[index]}'")
        else:
            result.append(f"Index {index} is out of bounds.")
    return result

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices_valid = [0, 7, 12]
    sample_indices_invalid = [-1, 50, 3]
    print("String:", sample_string)
    print("\nValid Indices:")
    valid_results = access_string_chars_by_indices(sample_string, sample_indices_valid)
    for result in valid_results:
        print(result)
    print("\nInvalid Indices:")
    invalid_results = access_string_chars_by_indices(sample_string, sample_indices_invalid)
    for result in invalid_results:
        print(result)