def separate_characters(input_string, delimiter):
    return delimiter.join(input_string)

if __name__ == '__main__':
    print(separate_characters("hello", "-"))