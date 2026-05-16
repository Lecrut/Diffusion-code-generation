def format_string(input_string):
    original = input_string
    all_caps = input_string.upper()
    sentence_case = ""
    if input_string:
        sentence_case = input_string[0].upper() + input_string[1:].lower()
    return f"{original}, {all_caps}, {sentence_case}"
if __name__ == '__main__':
    sample = "this is a sample sentence"
    result = format_string(sample)
    print(result)