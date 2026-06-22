def remove_spaces(strings):
    return [s.replace(" ", "") for s in strings]

if __name__ == '__main__':
    sample_strings = ["Hello World", "This is a test string", "Remove spaces"]
    result = remove_spaces(sample_strings)
    print(result)