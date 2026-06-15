import re
def count_words(text):
    if not text:
        return 0
    return len(re.findall(r'\b\w+\b', text))
if __name__ == '__main__':
    sample_string1 = "  Hello world!   This is a test. "
    sample_string2 = "Multiple   spaces\tand\nnewlines."
    sample_string3 = ""
    sample_string4 = "SingleWord"
    print(f"'{sample_string1}': {count_words(sample_string1)}")
    print(f"'{sample_string2}': {count_words(sample_string2)}")
    print(f"'{sample_string3}': {count_words(sample_string3)}")
    print(f"'{sample_string4}': {count_words(sample_string4)}")