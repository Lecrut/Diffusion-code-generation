def extract_characters_by_indices(input_string, indices):
    MAX_INDEX = len(input_string) - 1
    
    def is_valid_index(index):
        return isinstance(index, int) and 0 <= index <= MAX_INDEX
    
    if not all(is_valid_index(i) for i in indices):
        raise ValueError("All indices must be integers within the string's length range.")
    
    result = [input_string[i] for i in indices]
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud"
    sample_indices = [0, 2, 4, 7, 11]
    print(extract_characters_by_indices(sample_string, sample_indices))