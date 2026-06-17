import re
def count_words_with_punctuation(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)
if __name__ == '__main__':
    sample_string_1 = "Hello world! This is a test, how are you?"
    sample_string_2 = "One-two three... four five."
    sample_string_3 = "Word.Another,word?Final."
    sample_string_4 = "  leading and trailing spaces  "
    sample_string_5 = "SingleWord"
    print(f"'{sample_string_1}': {count_words_with_punctuation(sample_string_1)}")
    print(f"'{sample_string_2}': {count_words_with_punctuation(sample_string_2)}")
    print(f"'{sample_string_3}': {count_words_with_punctuation(sample_string_3)}")
    print(f"'{sample_string_4}': {count_words_with_punctuation(sample_string_4)}")
    print(f"'{sample_string_5}': {count_words_with_punctuation(sample_string_5)}")