def convert_to_title_case(strings):
    return [s.title() for s in strings]

if __name__ == '__main__':
    sample_strings = ["hello world", "python programming", "openai gpt-4"]
    title_cased_strings = convert_to_title_case(sample_strings)
    print(title_cased_strings)