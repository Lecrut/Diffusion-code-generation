def remove_internal_spaces(strings):
    return [s.replace(' ', '') for s in strings]

if __name__ == '__main__':
    sample_strings = ["hello world", "openai gpt-4", "remove spaces", "  extra spaces  "]
    result = remove_internal_spaces(sample_strings)
    print(result)