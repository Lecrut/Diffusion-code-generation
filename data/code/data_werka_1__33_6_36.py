def remove_internal_spaces(strings):
    return [''.join(s.split()) for s in strings]

if __name__ == '__main__':
    sample_values = ["hello world", "  python programming  ", "remove spaces", "  multiple   spaces  "]
    result = remove_internal_spaces(sample_values)
    print(result)