def char_index_map(hardcoded_string):
    return {char: index for index, char in enumerate(hardcoded_string)}

if __name__ == '__main__':
    sample_string = "hello"
    print(char_index_map(sample_string))