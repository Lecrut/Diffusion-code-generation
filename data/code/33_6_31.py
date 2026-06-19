def remove_spaces_from_strings(strings):
    return [s.replace(' ', '') for s in strings]

if __name__ == '__main__':
    sample_input = ["hello world", "this is a test", "remove spaces please"]
    result = remove_spaces_from_strings(sample_input)
    print(result)