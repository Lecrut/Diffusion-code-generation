def format_string(s):
    SEPARATOR = ", "
    original = s
    all_caps = s.upper()
    sentence_case = s.capitalize()
    return f"{original}{SEPARATOR}{all_caps}{SEPARATOR}{sentence_case}"

if __name__ == '__main__':
    SAMPLE_INPUT = "hello world"
    result = format_string(SAMPLE_INPUT)
    print(result)