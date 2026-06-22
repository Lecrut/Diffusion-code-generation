def remove_internal_spaces(strings):
    return [s.replace(' ', '') for s in strings]

if __name__ == '__main__':
    sample_input = ["hello world", "this is a test", "python programming"]
    result = remove_internal_spaces(sample_input)
    print(result)