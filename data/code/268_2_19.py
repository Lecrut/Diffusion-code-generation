def extract_first_word(text: str) -> str:
    if not text.strip():
        raise ValueError("Input string cannot be empty or contain only whitespace.")
    words = text.split()
    return words[0]

if __name__ == '__main__':
    sample_string_1 = "Hello world, this is a test."
    sample_string_2 = "singleword"
    sample_string_3 = "   leading spaces and multiple words "
    sample_string_4 = ""
    sample_string_5 = "  "

    try:
        result_1 = extract_first_word(sample_string_1)
        print(f"Input: '{sample_string_1}' -> Output: '{result_1}'")
    except ValueError as e:
        print(e)

    try:
        result_2 = extract_first_word(sample_string_2)
        print(f"Input: '{sample_string_2}' -> Output: '{result_2}'")
    except ValueError as e:
        print(e)

    try:
        result_3 = extract_first_word(sample_string_3)
        print(f"Input: '{sample_string_3}' -> Output: '{result_3}'")
    except ValueError as e:
        print(e)

    try:
        result_4 = extract_first_word(sample_string_4)
        print(f"Input: '{sample_string_4}' -> Output: '{result_4}'")
    except ValueError as e:
        print(e)

    try:
        result_5 = extract_first_word(sample_string_5)
        print(f"Input: '{sample_string_5}' -> Output: '{result_5}'")
    except ValueError as e:
        print(e)