def replace_spaces_with_underscores(text):
    result = []
    for char in text:
        if char == ' ':
            result.append('_')
        else:
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    sample_string = "Hello World This Is A Test"
    transformed_string = replace_spaces_with_underscores(sample_string)
    print(transformed_string)