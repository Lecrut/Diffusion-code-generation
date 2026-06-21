def create_char_index_mapping(hardcoded_string):
    char_map = {}
    for index, char in enumerate(hardcoded_string):
        if char not in char_map:
            char_map[char] = index
    return char_map

if __name__ == '__main__':
    sample_string = "programming"
    result = create_char_index_mapping(sample_string)
    print(result)