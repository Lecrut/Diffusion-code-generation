def print_characters_by_indices(s, indices):
    if not isinstance(s, str) or not all(isinstance(i, int) for i in indices):
        raise ValueError("Invalid input types")
    
    result = []
    for index in indices:
        if 0 <= index < len(s):
            result.append(s[index])
        else:
            result.append(None)
    
    return result

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices = [0, 7, 12, 5, 10]
    print(print_characters_by_indices(sample_string, sample_indices))