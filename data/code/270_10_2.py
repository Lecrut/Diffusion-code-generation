def remove_spaces(strings):
    return [s.replace(' ', '') for s in strings]

if __name__ == '__main__':
    sample_strings = ["Hello World", "Python Programming", "Remove Spaces"]
    result = remove_spaces(sample_strings)
    print(result)