def clean_strings(strings):
    return [s.strip() for s in strings]

if __name__ == '__main__':
    sample_data = ["  hello  ", "\tworld\n", "  ", "no_space", "  leading_trailing  "]
    result = clean_strings(sample_data)
    print(result)