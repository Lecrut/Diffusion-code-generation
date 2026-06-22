import re

def count_words(text):
    if not text:
        return 0
    words = re.findall(r'\b\w+\b', text)
    return len(words)

if __name__ == '__main__':
    sample_string1 = "This is a test string with multiple spaces."
    sample_string2 = "  leading and trailing spaces   \tand newlines\n"
    sample_string3 = ""
    sample_string4 = "OneWord"
    sample_string5 = "word1  word2\tword3"

    print(f"'{sample_string1}': {count_words(sample_string1)}")
    print(f"'{sample_string2}': {count_words(sample_string2)}")
    print(f"'{sample_string3}': {count_words(sample_string3)}")
    print(f"'{sample_string4}': {count_words(sample_string4)}")
    print(f"'{sample_string5}': {count_words(sample_string5)}")