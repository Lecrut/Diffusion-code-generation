def validate_string_and_indices(s, indices):
    if not isinstance(s, str):
        raise ValueError("The first argument must be a string.")
    if not all(isinstance(i, int) for i in indices):
        raise ValueError("All elements in the second argument must be integers.")
    valid_range = 0 <= i < len(s)
    if not all(valid_range for i in indices):
        raise ValueError("All indices must be within the bounds of the string length.")

def print_characters_by_indices(s, indices):
    validate_string_and_indices(s, indices)
    result = ''.join(s[i] for i in indices)
    return result

if __name__ == '__main__':
    sample_string = "Alibaba Cloud"
    sample_indices = [0, 4, 5, 11]
    print(print_characters_by_indices(sample_string, sample_indices))