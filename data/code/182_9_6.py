def create_char_index_mapping(hardcoded_string):
    if not isinstance(hardcoded_string, str):
        raise ValueError("Input must be a string")
    
    return {char: index for index, char in enumerate(hardcoded_string)}

if __name__ == '__main__':
    sample_string = "hello"
    print(create_char_index_mapping(sample_string))