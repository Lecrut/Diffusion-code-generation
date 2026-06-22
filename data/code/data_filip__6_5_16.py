def replace_spaces_with_underscores():
    original_string = "hello world foo bar"
    modified_string = original_string.replace(" ", "_")
    return modified_string

if __name__ == '__main__':
    print(replace_spaces_with_underscores())