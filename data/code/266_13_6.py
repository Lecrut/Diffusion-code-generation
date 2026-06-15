import re
def count_words(text):
    return len(text.split())
if __name__ == '__main__':
    test_string1 = "This is a sample sentence"
    test_string2 = "  leading and trailing spaces "
    test_string3 = "Multiple   spaces between words"
    test_string4 = ""
    test_string5 = "SingleWord"
    print(f"'{test_string1}': {count_words(test_string1)}")
    print(f"'{test_string2}': {count_words(test_string2)}")
    print(f"'{test_string3}': {count_words(test_string3)}")
    print(f"'{test_string4}': {count_words(test_string4)}")
    print(f"'{test_string5}': {count_words(test_string5)}")