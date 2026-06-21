def separate_characters(s):
    return [(i, char) for i, char in enumerate(s)]

if __name__ == '__main__':
    sample_string = "hello"
    result = separate_characters(sample_string)
    print(result)