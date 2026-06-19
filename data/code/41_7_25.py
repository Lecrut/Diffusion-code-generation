def format_string_versions(input_string):
    all_caps = input_string.upper()
    sentence_case = input_string.capitalize()
    return f"{input_string}, {all_caps}, {sentence_case}"

if __name__ == '__main__':
    sample_input = "hello world"
    formatted_output = format_string_versions(sample_input)
    print(formatted_output)