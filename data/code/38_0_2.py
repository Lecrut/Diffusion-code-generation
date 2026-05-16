import string
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
    test_string_1 = "hello world"
    test_string_2 = "programming"
    test_string_3 = "abcdefg"
    test_string_4 = "aabbccddeeff"
    print(f"Input: '{test_string_1}'")
    print("Repeated letters found:", find_repeated_letters(test_string_1))
    print("-" * 20)
    print(f"Input: '{test_string_2}'")
    print("Repeated letters found:", find_repeated_letters(test_string_2))
    print("-" * 20)
    print(f"Input: '{test_string_3}'")
    print("Repeated letters found:", find_repeated_letters(test_string_3))
    print("-" * 20)
    print(f"Input: '{test_string_4}'")
    print("Repeated letters found:", find_repeated_letters(test_string_4))
    print("-" * 20)