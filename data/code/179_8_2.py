def reverse_word_order(text):
    words = text.split()
    words.reverse()
    return " ".join(words)
if __name__ == '__main__':
    test_string1 = "  hello   world  "
    result1 = reverse_word_order(test_string1)
    print(f"Input: '{test_string1}'")
    print(f"Output: '{result1}'")
    test_string2 = "  a   b c  d "
    result2 = reverse_word_order(test_string2)
    print(f"Input: '{test_string2}'")
    print(f"Output: '{result2}'")
    test_string3 = "singleword"
    result3 = reverse_word_order(test_string3)
    print(f"Input: '{test_string3}'")
    print(f"Output: '{result3}'")
    test_string4 = "  multiple   spaces   here "
    result4 = reverse_word_order(test_string4)
    print(f"Input: '{test_string4}'")
    print(f"Output: '{result4}'")