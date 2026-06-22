def extract_characters_by_indices(s, indices):
    if not isinstance(s, str):
        raise ValueError("The first argument must be a string.")
    if not all(isinstance(i, int) for i in indices):
        raise ValueError("All elements in the second argument must be integers.")
    
    valid_indices = [i for i in indices if 0 <= i < len(s)]
    characters = [s[i] for i in valid_indices]
    return ''.join(characters)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud"
    sample_indices = [2, 5, 8, 10]
    print(extract_characters_by_indices(sample_string, sample_indices))