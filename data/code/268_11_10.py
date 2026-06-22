def get_first_word(text):
    words = text.split()
    if not words:
        raise ValueError("Input string is empty or contains only whitespace.")
    return words[0]

if __name__ == '__main__':
    test_string1 = "Hello world"
    try:
        print(f"Input: '{test_string1}', Output: '{get_first_word(test_string1)}'")
    except ValueError as e:
        print(e)

    test_string2 = "   leading spaces and multiple words"
    try:
        print(f"Input: '{test_string2}', Output: '{get_first_word(test_string2)}'")
    except ValueError as e:
        print(e)

    test_string3 = "singleword"
    try:
        print(f"Input: '{test_string3}', Output: '{get_first_word(test_string3)}'")
    except ValueError as e:
        print(e)

    test_string4 = ""
    try:
        print(f"Input: '{test_string4}', Output: '{get_first_word(test_string4)}'")
    except ValueError as e:
        print(e)

    test_string5 = "  "
    try:
        print(f"Input: '{test_string5}', Output: '{get_first_word(test_string5)}'")
    except ValueError as e:
        print(e)