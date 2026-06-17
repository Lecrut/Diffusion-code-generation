import re
def count_words(text):
    return len(text.split())
if __name__ == '__main__':
    test_string1 = "This is a sample sentence."
    test_string2 = "  Multiple   spaces   here."
    test_string3 = ""
    test_string4 = "SingleWord"
    test_string5 = "Word1 Word2\nWord3"
    print(f"'{test_string1}': {count_words(test_string1)}")
    print(f"'{test_string2}': {count_words(test_string2)}")
    print(f"'{test_string3}': {count_words(test_string3)}")
    print(f"'{test_string4}': {count_words(test_string4)}")
    print(f"'{test_string5}': {count_words(test_string5)}")