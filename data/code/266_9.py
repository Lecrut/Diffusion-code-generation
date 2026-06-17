import re
def count_words_with_punctuation(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)
if __name__ == '__main__':
    sample1 = "Hello world! This is a test."
    sample2 = "What's up, world? How are you?"
    sample3 = "One-two-three... four five."
    sample4 = "  leading and trailing spaces   "
    sample5 = "Hyphenated-words are tricky."
    print(f"'{sample1}' -> {count_words_with_punctuation(sample1)}")
    print(f"'{sample2}' -> {count_words_with_punctuation(sample2)}")
    print(f"'{sample3}' -> {count_words_with_punctuation(sample3)}")
    print(f"'{sample4}' -> {count_words_with_punctuation(sample4)}")
    print(f"'{sample5}' -> {count_words_with_punctuation(sample5)}")