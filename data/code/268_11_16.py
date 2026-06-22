def get_first_word(text):
    words = text.split()
    if not words:
        return ""
    return words[0]

if __name__ == '__main__':
    test_string1 = "Hello world"
    result1 = get_first_word(test_string1)
    print(f"Input: '{test_string1}', Output: '{result1}'")
    
    test_string2 = "   leading spaces and multiple words"
    result2 = get_first_word(test_string2)
    print(f"Input: '{test_string2}', Output: '{result2}'")
    
    test_string3 = "singleword"
    result3 = get_first_word(test_string3)
    print(f"Input: '{test_string3}', Output: '{result3}'")
    
    test_string4 = ""
    result4 = get_first_word(test_string4)
    print(f"Input: '{test_string4}', Output: '{result4}'")