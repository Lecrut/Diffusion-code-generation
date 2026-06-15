import re
def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)
if __name__ == '__main__':
    sample1 = "This is a test sentence with some punctuation."
    sample2 = "Hello, world! How are you doing today?"
    sample3 = "One-two-three... four five six."
    sample4 = "  leading and trailing spaces   "
    sample5 = "Hyphenated-words and apostrophes' count."
    print(f"'{sample1}' -> {count_words(sample1)}")
    print(f"'{sample2}' -> {count_words(sample2)}")
    print(f"'{sample3}' -> {count_words(sample3)}")
    print(f"'{sample4}' -> {count_words(sample4)}")
    print(f"'{sample5}' -> {count_words(sample5)}")