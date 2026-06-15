import re
def find_unique_words(text):
    words = set(re.findall(r'\b\w+\b', text.lower()))
    return words
if __name__ == '__main__':
    sample_string = "Hello world! This is a test string, with various delimiters and punctuation."
    unique_words = find_unique_words(sample_string)
    print(unique_words)