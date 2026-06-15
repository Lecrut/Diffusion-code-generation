import re
def separate_words(text):
    words = re.findall(r'\b\w+\b', text)
    return words
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, with spaces and punctuation."
    sample_string2 = "  \tWord1... Word2? End. "
    sample_string3 = "One-two-three... four"
    result1 = separate_words(sample_string1)
    result2 = separate_words(sample_string2)
    result3 = separate_words(sample_string3)
    print(f"'{sample_string1}' -> {result1}")
    print(f"'{sample_string2}' -> {result2}")
    print(f"'{sample_string3}' -> {result3}")