def replace_spaces_with_underscores(text):
    return text.replace(" ", "_")

if __name__ == '__main__':
    original_string = "hello world python"
    result = replace_spaces_with_underscores(original_string)
    print(result)