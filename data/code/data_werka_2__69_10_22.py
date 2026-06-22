def print_characters_by_indices(input_string, indices):
    if not all(isinstance(i, int) and 0 <= i < len(input_string) for i in indices):
        raise ValueError("All indices must be integers within the bounds of the string length.")
    
    result = ''.join(input_string[i] for i in indices)
    print(result)

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices = [0, 7, 8, 12]
    print_characters_by_indices(sample_string, sample_indices)