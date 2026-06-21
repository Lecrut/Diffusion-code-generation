def separate_words(text):
    return text.split()

if __name__ == '__main__':
    test_string1 = "  hello world  "
    result1 = separate_words(test_string1)
    print(f"Input: '{test_string1}'")
    print(f"Output: {result1}")
    
    test_string2 = "multiple   spaces   here"
    result2 = separate_words(test_string2)
    print(f"Input: '{test_string2}'")
    print(f"Output: {result2}")
    
    test_string3 = "singleword"
    result3 = separate_words(test_string3)
    print(f"Input: '{test_string3}'")
    print(f"Output: {result3}")
    
    test_string4 = "   leading and trailing spaces   "
    result4 = separate_words(test_string4)
    print(f"Input: '{test_string4}'")
    print(f"Output: {result4}")