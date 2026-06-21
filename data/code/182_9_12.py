def char_index_mapping(hardcoded_string):
    return {char: index for index, char in enumerate(hardcoded_string)}

if __name__ == '__main__':
    sample_string = "example"
    print(char_index_mapping(sample_string))