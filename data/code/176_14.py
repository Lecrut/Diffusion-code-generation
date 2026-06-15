import re
def find_all_words(text):
    words = set()
    for char in text:
        if char.isalpha():
            words.add(char.lower())
    return list(words)
if __name__ == '__main__':
    sample_string = "Hello world! This is a test, with mixed cases and numbers 123."
    result = find_all_words(sample_string)
    print(result)