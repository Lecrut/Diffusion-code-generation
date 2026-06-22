def find_repeated_letters(input_string):
    seen_letters = set()
    repeated_letters = set()
    for char in input_string:
        if 'a' <= char.lower() <= 'z':
            if char in seen_letters:
                repeated_letters.add(char)
            else:
                seen_letters.add(char)
    return sorted(list(repeated_letters))

if __name__ == '__main__':
    SAMPLE_STRING_1 = "programming"
    SAMPLE_STRING_2 = "hello world"
    SAMPLE_STRING_3 = "abcdefg"
    SAMPLE_STRING_4 = "aabbccddeeff"

    print(f"Input: '{SAMPLE_STRING_1}'")
    print("Repeated letters found:", find_repeated_letters(SAMPLE_STRING_1))

    print(f"\nInput: '{SAMPLE_STRING_2}'")
    print("Repeated letters found:", find_repeated_letters(SAMPLE_STRING_2))

    print(f"\nInput: '{SAMPLE_STRING_3}'")
    print("Repeated letters found:", find_repeated_letters(SAMPLE_STRING_3))

    print(f"\nInput: '{SAMPLE_STRING_4}'")
    print("Repeated letters found:", find_repeated_letters(SAMPLE_STRING_4))