def extract_characters_by_indices(input_string, index_list):
    if not isinstance(input_string, str) or not all(isinstance(i, int) for i in index_list):
        raise ValueError("Invalid input types")
    
    valid_indices = [i for i in index_list if 0 <= i < len(input_string)]
    character_list = [input_string[i] for i in valid_indices]
    
    return ''.join(character_list)

if __name__ == '__main__':
    test_string = "Python Programming"
    test_indices = [1, 6, 7, 15, 20]
    extracted_characters = extract_characters_by_indices(test_string, test_indices)
    print(extracted_characters)