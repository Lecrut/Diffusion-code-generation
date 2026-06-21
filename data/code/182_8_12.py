def separate_characters(s):
    return [(i, char) for i, char in enumerate(s)]

if __name__ == '__main__':
    sample_string = "hello"
    print(separate_characters(sample_string))