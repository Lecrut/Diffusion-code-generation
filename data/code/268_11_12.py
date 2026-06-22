def is_valid_text(text):
    return isinstance(text, str)

def get_first_word(text):
    if not is_valid_text(text):
        raise ValueError("Input must be a string")
    
    words = text.split()
    if words:
        return words[0]
    else:
        return ""

if __name__ == '__main__':
    test_string_1 = "Hello world"
    print(f"Input: '{test_string_1}', Output: '{get_first_word(test_string_1)}'")
    
    test_string_2 = "   leading spaces and multiple words"
    print(f"Input: '{test_string_2}', Output: '{get_first_word(test_string_2)}'")
    
    test_string_3 = "singleword"
    print(f"Input: '{test_string_3}', Output: '{get_first_word(test_string_3)}'")
    
    test_string_4 = ""
    print(f"Input: '{test_string_4}', Output: '{get_first_word(test_string_4)}'")
    
    test_string_5 = "  "
    print(f"Input: '{test_string_5}', Output: '{get_first_word(test_string_5)}'")