def format_string(s):
    original = s
    all_caps = s.upper()
    sentence_case = s.capitalize()
    return f"{original}, {all_caps}, {sentence_case}"

if __name__ == '__main__':
    sample_string = "hello world"
    formatted_string = format_string(sample_string)
    print(formatted_string)