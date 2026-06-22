def remove_internal_spaces(strings):
    return [s.replace(' ', '') for s in strings]

if __name__ == '__main__':
    sample_values = ["hello world", "this is a test", "remove spaces"]
    result = remove_internal_spaces(sample_values)
    print(result)