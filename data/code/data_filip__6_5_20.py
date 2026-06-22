def convert_spaces_to_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample_string = "Hello World Python"
    result = convert_spaces_to_underscores(sample_string)
    print(result)