def split_string_to_words(text):
    if not text:
        return []
    words = text.split()
    return words
if __name__ == '__main__':
    test_string1 = "  hello world  "
    result1 = split_string_to_words(test_string1)
    print(f"Input: '{test_string1}'")
    print(f"Output: {result1}")
    test_string2 = "multiple   spaces here"
    result2 = split_string_to_words(test_string2)
    print(f"Input: '{test_string2}'")
    print(f"Output: {result2}")
    test_string3 = " leading and trailing "
    result3 = split_string_to_words(test_string3)
    print(f"Input: '{test_string3}'")
    print(f"Output: {result3}")
    test_string4 = ""
    result4 = split_string_to_words(test_string4)
    print(f"Input: '{test_string4}'")
    print(f"Output: {result4}")
    test_string5 = "singleword"
    result5 = split_string_to_words(test_string5)
    print(f"Input: '{test_string5}'")
    print(f"Output: {result5}")