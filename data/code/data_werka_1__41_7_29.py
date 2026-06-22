def format_string(s):
    all_caps = s.upper()
    sentence_case = s.capitalize()
    return f"{s}, {all_caps}, {sentence_case}"

if __name__ == '__main__':
    sample_string = "hello world"
    formatted_result = format_string(sample_string)
    print(formatted_result)