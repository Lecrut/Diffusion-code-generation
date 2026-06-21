def separate_characters(s):
    return list(enumerate(s))

if __name__ == '__main__':
    sample_string = "hello"
    result = separate_characters(sample_string)
    print(result)