import re
def count_words(text):
    if not text:
        return 0
    return len(re.findall(r'\b\w+\b', text))
if __name__ == '__main__':
    sample1 = "This is a sample sentence."
    sample2 = "Another test string with multiple words."
    sample3 = ""
    sample4 = "  leading and trailing spaces are handled correctly. "
    sample5 = "Word1, Word2; Word3"
    print(f"'{sample1}' -> {count_words(sample1)}")
    print(f"'{sample2}' -> {count_words(sample2)}")
    print(f"'{sample3}' -> {count_words(sample3)}")
    print(f"'{sample4}' -> {count_words(sample4)}")
    print(f"'{sample5}' -> {count_words(sample5)}")