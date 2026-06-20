def replace_spaces_with_underscores(text):
    return text.replace(" ", "_")

if __name__ == '__main__':
    test_string = "Hello World Python"
    result = replace_spaces_with_underscores(test_string)
    print(result)