def separate_chars(input_string, delimiter):
    return delimiter.join(input_string)

if __name__ == '__main__':
    result = separate_chars("hello", ", ")
    print(result)