def reverse_words(s):
    words = s.split()
    words.reverse()
    return " ".join(words)
if __name__ == '__main__':
    test_string1 = "hello world"
    print(f"Input: '{test_string1}'")
    print(f"Output: '{reverse_words(test_string1)}'")
    test_string2 = "the quick brown fox"
    print(f"Input: '{test_string2}'")
    print(f"Output: '{reverse_words(test_string2)}'")
    test_string3 = "  multiple   spaces here "
    print(f"Input: '{test_string3}'")
    print(f"Output: '{reverse_words(test_string3)}'")
    test_string4 = "a b c"
    print(f"Input: '{test_string4}'")
    print(f"Output: '{reverse_words(test_string4)}'")