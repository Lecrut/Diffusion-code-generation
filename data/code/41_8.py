def format_string(input_string):
    original = input_string
    all_caps = input_string.upper()
    sentence_case = ""
    if original:
        sentence_case = original[0].upper() + original[1:].lower()
    else:
        sentence_case = ""
    return f"{original}, {all_caps}, {sentence_case}"
if __name__ == '__main__':
    sample = "this is a sample sentence"
    result = format_string(sample)
    print(result)