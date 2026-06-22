def remove_spaces_from_strings(strings):
    return [s.replace(' ', '') for s in strings]

if __name__ == '__main__':
    sample_values = ["hello world", "  python programming  ", "remove spaces"]
    result = remove_spaces_from_strings(sample_values)
    print(result)