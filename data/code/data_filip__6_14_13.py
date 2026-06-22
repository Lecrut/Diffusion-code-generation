def replace_spaces_with_underscores(text):
    result = ""
    for char in text:
        if char == ' ':
            result += '_'
        else:
            result += char
    return result

if __name__ == '__main__':
    sample_text = "Hello World Python"
    transformed_text = replace_spaces_with_underscores(sample_text)
    print(transformed_text)