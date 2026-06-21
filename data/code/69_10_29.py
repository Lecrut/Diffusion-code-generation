def print_characters_by_indices(input_string, indices):
    if not all(isinstance(i, int) for i in indices):
        raise ValueError("All elements in the list must be integers.")
    if any(i < 0 or i >= len(input_string) for i in indices):
        raise ValueError("Index out of range.")
    
    result = ''.join(input_string[i] for i in indices)
    print(result)

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices = [0, 7, 8, 12]
    print_characters_by_indices(sample_string, sample_indices)