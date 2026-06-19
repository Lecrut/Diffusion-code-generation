def convert_to_title_case(strings):
    return [s.title() for s in strings]

if __name__ == '__main__':
    sample_input = ["hello world", "python programming", "openai gpt-4"]
    result = convert_to_title_case(sample_input)
    print(result)