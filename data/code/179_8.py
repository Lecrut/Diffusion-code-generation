def reverse_word_order(text):
    words = text.split()
    words.reverse()
    return " ".join(words)
if __name__ == '__main__':
    test_string1 = "  hello   world  "
    test_string2 = "a b c d"
    test_string3 = "singleword"
    test_string4 = "   leading and trailing spaces   "
    test_string5 = ""
    print(f"Input: '{test_string1}' -> Output: '{reverse_word_order(test_string1)}'")
    print(f"Input: '{test_string2}' -> Output: '{reverse_word_order(test_string2)}'")
    print(f"Input: '{test_string3}' -> Output: '{reverse_word_order(test_string3)}'")
    print(f"Input: '{test_string4}' -> Output: '{reverse_word_order(test_string4)}'")
    print(f"Input: '{test_string5}' -> Output: '{reverse_word_order(test_string5)}'")