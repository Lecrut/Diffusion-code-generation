def remove_internal_spaces(strings):
    return [s.replace(' ', '') for s in strings]

if __name__ == '__main__':
    sample_input = ["hello world", "openai gpt-4", "remove spaces"]
    result = remove_internal_spaces(sample_input)
    print(result)