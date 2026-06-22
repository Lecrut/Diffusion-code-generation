def remove_spaces(input_string):
    return ''.join(input_string.split())

if __name__ == '__main__':
    sample_input = "Hello World"
    print(remove_spaces(sample_input))