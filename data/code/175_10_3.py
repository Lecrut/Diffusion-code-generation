def separate_words(text):
    return text.split()
if __name__ == '__main__':
    test_string1 = "  hello world  "
    result1 = separate_words(test_string1)
    print(result1)
    test_string2 = "multiple   spaces   here"
    result2 = separate_words(test_string2)
    print(result2)
    test_string3 = "singleword"
    result3 = separate_words(test_string3)
    print(result3)
    test_string4 = "   leading and trailing  "
    result4 = separate_words(test_string4)
    print(result4)