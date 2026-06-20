def replace_spaces_with_underscores(s):
    return s.replace(' ', '_')

if __name__ == '__main__':
    input_string = "Hello World Python"
    result = replace_spaces_with_underscores(input_string)
    print(result)