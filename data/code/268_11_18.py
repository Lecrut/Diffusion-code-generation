def get_first_word(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    if not words:
        return ""
    return words[0]

if __name__ == '__main__':
    test_string1 = "Hello world"
    print(f"Input: '{test_string1}', Output: '{get_first_word(test_string1)}'")
    test_string2 = "   leading spaces and multiple words"
    print(f"Input: '{test_string2}', Output: '{get_first_word(test_string2)}'")
    test_string3 = "singleword"
    print(f"Input: '{test_string3}', Output: '{get_first_word(test_string3)}'")
    test_string4 = ""
    print(f"Input: '{test_string4}', Output: '{get_first_word(test_string4)}'")
    test_string5 = "  "
    print(f"Input: '{test_string5}', Output: '{get_first_word(test_string5)}'")