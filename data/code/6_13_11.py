def replace_spaces_with_underscores(constant_string):
    return constant_string.replace(' ', '_')

if __name__ == '__main__':
    constant_string = "hello world example"
    result = replace_spaces_with_underscores(constant_string)
    print(result)