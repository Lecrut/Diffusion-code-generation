def capitalize_first_letter_only(text):
    if not text:
        return ""
    return text[0].upper() + text[1:]
if __name__ == '__main__':
    sample_text_1 = "hello world"
    result_1 = capitalize_first_letter_only(sample_text_1)
    print(f"Input: '{sample_text_1}'")
    print(f"Output: '{result_1}'")
    sample_text_2 = "this is a test sentence"
    result_2 = capitalize_first_letter_only(sample_text_2)
    print(f"Input: '{sample_text_2}'")
    print(f"Output: '{result_2}'")
    sample_text_3 = "a"
    result_3 = capitalize_first_letter_only(sample_text_3)
    print(f"Input: '{sample_text_3}'")
    print(f"Output: '{result_3}'")
    sample_text_4 = ""
    result_4 = capitalize_first_letter_only(sample_text_4)
    print(f"Input: '{sample_text_4}'")
    print(f"Output: '{result_4}'")