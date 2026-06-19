def remove_internal_spaces(strings):
    return [s.replace(' ', '') for s in strings]

if __name__ == '__main__':
    sample_strings = ["hello world", "this is a test", "remove spaces here"]
    result = remove_internal_spaces(sample_strings)
    print(result)