import re
def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)
if __name__ == '__main__':
    sample_string_1 = "This is a sample string with various spaces."
    sample_string_2 = "  Multiple   spaces   and    extra   whitespace. "
    sample_string_3 = "SingleWord"
    sample_string_4 = ""
    sample_string_5 = "Words\tseparated\nby\nnewlines."
    print(f"'{sample_string_1}': {count_words(sample_string_1)}")
    print(f"'{sample_string_2}': {count_words(sample_string_2)}")
    print(f"'{sample_string_3}': {count_words(sample_string_3)}")
    print(f"'{sample_string_4}': {count_words(sample_string_4)}")
    print(f"'{sample_string_5}': {count_words(sample_string_5)}")