def format_string(text):
    original = text
    all_caps = text.upper()
    sentence_case = text.capitalize()
    return f"{original}, {all_caps}, {sentence_case}"
if __name__ == '__main__':
    sample_string = "this is a sample sentence"
    result = format_string(sample_string)
    print(result)