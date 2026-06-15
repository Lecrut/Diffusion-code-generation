import re
def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, how are you?"
    sample_string2 = "One-two three... four five."
    sample_string3 = "  Leading spaces and trailing punctuation."
    sample_string4 = "SingleWord"
    print(f"'{sample_string1}' -> {count_words(sample_string1)}")
    print(f"'{sample_string2}' -> {count_words(sample_string2)}")
    print(f"'{sample_string3}' -> {count_words(sample_string3)}")
    print(f"'{sample_string4}' -> {count_words(sample_string4)}")