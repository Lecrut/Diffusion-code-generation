def convert_spaces_to_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    input_string = "Hello World Python"
    result = convert_spaces_to_underscores(input_string)
    print(result)