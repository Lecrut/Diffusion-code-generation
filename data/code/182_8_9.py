def separate_characters(s):
    result = []
    for index, value in enumerate(s):
        result.append((index, value))
    return result

if __name__ == '__main__':
    sample_string = "hello"
    print(separate_characters(sample_string))