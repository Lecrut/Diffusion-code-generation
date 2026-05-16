def capitalize_first_letter_only(text: str) -> str:
    if not text:
        return ""
    return text[0].upper() + text[1:]
if __name__ == '__main__':
    sample_text_1 = "hello world this is a test"
    result_1 = capitalize_first_letter_only(sample_text_1)
    print(f"Original: {sample_text_1}")
    print(f"Result: {result_1}")
    sample_text_2 = "python programming is fun"
    result_2 = capitalize_first_letter_only(sample_text_2)
    print(f"Original: {sample_text_2}")
    print(f"Result: {result_2}")
    sample_text_3 = "a"
    result_3 = capitalize_first_letter_only(sample_text_3)
    print(f"Original: {sample_text_3}")
    print(f"Result: {result_3}")
    sample_text_4 = ""
    result_4 = capitalize_first_letter_only(sample_text_4)
    print(f"Original: '{sample_text_4}'")
    print(f"Result: '{result_4}'")