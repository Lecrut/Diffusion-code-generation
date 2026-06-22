def format_string(s):
    all_caps = s.upper()
    sentence_case = s.capitalize()
    return f"{s}, {all_caps}, {sentence_case}"

if __name__ == '__main__':
    sample_input = "hello world"
    formatted_output = format_string(sample_input)
    print(formatted_output)