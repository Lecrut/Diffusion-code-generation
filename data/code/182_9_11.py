def char_index_mapping(input_string):
    return {char: index for index, char in enumerate(input_string)}

if __name__ == '__main__':
    sample_string = "hello"
    print(char_index_mapping(sample_string))