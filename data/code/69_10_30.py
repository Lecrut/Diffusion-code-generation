def print_characters_by_indices(input_string, indices):
    if not isinstance(input_string, str) or not all(isinstance(i, int) for i in indices):
        raise ValueError("Invalid input types")
    
    result = []
    for index in indices:
        if 0 <= index < len(input_string):
            result.append(input_string[index])
        else:
            result.append(None)
    
    return result

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices = [0, 7, 12, 5, 15]
    print(print_characters_by_indices(sample_string, sample_indices))