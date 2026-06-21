def create_char_index_dict(input_string):
    return {char: index for index, char in enumerate(input_string)}

if __name__ == '__main__':
    sample_string = "example"
    print(create_char_index_dict(sample_string))