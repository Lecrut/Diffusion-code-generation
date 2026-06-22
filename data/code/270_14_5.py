def remove_spaces(strings):
    return [s.replace(' ', '') for s in strings]

if __name__ == '__main__':
    sample_values = ["hello world", "Python programming", "remove spaces"]
    result = remove_spaces(sample_values)
    print(result)