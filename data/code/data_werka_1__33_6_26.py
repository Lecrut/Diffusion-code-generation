def remove_internal_spaces(strings):
    return [s.replace(' ', '') for s in strings]

if __name__ == '__main__':
    sample_input = ["hello world", "open ai", "remove spaces", "test case"]
    result = remove_internal_spaces(sample_input)
    print(result)