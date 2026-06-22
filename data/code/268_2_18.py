def extract_first_word(text: str) -> str:
    if not text.strip():
        return ""
    return text.split()[0]

if __name__ == '__main__':
    sample_string_1 = "Hello world, this is a test."
    sample_string_2 = "singleword"
    sample_string_3 = "   leading spaces and multiple words "
    sample_string_4 = ""
    sample_string_5 = "  "

    result_1 = extract_first_word(sample_string_1)
    result_2 = extract_first_word(sample_string_2)
    result_3 = extract_first_word(sample_string_3)
    result_4 = extract_first_word(sample_string_4)
    result_5 = extract_first_word(sample_string_5)

    print(f"Input: '{sample_string_1}' -> Output: '{result_1}'")
    print(f"Input: '{sample_string_2}' -> Output: '{result_2}'")
    print(f"Input: '{sample_string_3}' -> Output: '{result_3}'")
    print(f"Input: '{sample_string_4}' -> Output: '{result_4}'")
    print(f"Input: '{sample_string_5}' -> Output: '{result_5}'")