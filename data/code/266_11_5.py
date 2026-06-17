import re
def count_words(text):
    return len(text.split())
if __name__ == '__main__':
    sample_string_1 = "This is a sample string for testing"
    sample_string_2 = "  leading and trailing spaces are handled well "
    sample_string_3 = "OneWord"
    sample_string_4 = ""
    sample_string_5 = "Multiple   spaces\tand\nnewlines"
    print(f"'{sample_string_1}': {count_words(sample_string_1)}")
    print(f"'{sample_string_2}': {count_words(sample_string_2)}")
    print(f"'{sample_string_3}': {count_words(sample_string_3)}")
    print(f"'{sample_string_4}': {count_words(sample_string_4)}")
    print(f"'{sample_string_5}': {count_words(sample_string_5)}")