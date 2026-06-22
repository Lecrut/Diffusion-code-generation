def remove_spaces(input_string):
    return ''.join(filter(lambda x: x != ' ', input_string))

if __name__ == '__main__':
    sample_input = "Hello World"
    print(remove_spaces(sample_input))