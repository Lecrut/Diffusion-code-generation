def replace_spaces_with_underscores(input_string):
    return input_string.replace(" ", "_")

if __name__ == '__main__':
    result = replace_spaces_with_underscores("Hello World")
    print(result)