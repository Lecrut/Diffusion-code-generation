def remove_spaces(strings):
    return [s.replace(' ', '') for s in strings]

if __name__ == '__main__':
    input_strings = ["Hello World", "Python Programming", "Remove Spaces"]
    processed_strings = remove_spaces(input_strings)
    print(processed_strings)