def fetch_characters_by_indices(input_string, indices):
    if not isinstance(input_string, str):
        raise ValueError("The first argument must be a string.")
    if not all(isinstance(i, int) for i in indices):
        raise ValueError("All elements in the second argument must be integers.")
    
    def is_valid_index(index):
        return 0 <= index < len(input_string)
    
    valid_indices = filter(is_valid_index, indices)
    result = ''.join(input_string[i] for i in valid_indices)
    return result

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices = [0, 7, 8, 12, 5]
    print(fetch_characters_by_indices(sample_string, sample_indices))