import re
def reverse_words(text):
    words = text.split()
    words.reverse()
    return " ".join(words)
if __name__ == '__main__':
    test_string1 = "  hello world  "
    test_string2 = "this   is   a   test"
    test_string3 = "singleword"
    test_string4 = "  multiple   spaces   here "
    test_string5 = ""
    print(f"Input: '{test_string1}' -> Output: '{reverse_words(test_string1)}'")
    print(f"Input: '{test_string2}' -> Output: '{reverse_words(test_string2)}'")
    print(f"Input: '{test_string3}' -> Output: '{reverse_words(test_string3)}'")
    print(f"Input: '{test_string4}' -> Output: '{reverse_words(test_string4)}'")
    print(f"Input: '{test_string5}' -> Output: '{reverse_words(test_string5)}'")