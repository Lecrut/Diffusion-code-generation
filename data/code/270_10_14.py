def remove_spaces(strings):
    return [s.replace(' ', '') for s in strings]

if __name__ == '__main__':
    input_strings = ["This is a test", "Multiple   spaces here"]
    result = remove_spaces(input_strings)
    print(result)