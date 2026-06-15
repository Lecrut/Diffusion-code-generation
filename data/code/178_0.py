import string
def extract_words(text):
    words = []
    for char in text:
        if char.isalpha() or char.isspace():
            words.append(char)
    processed_words = []
    for word in words:
        if word.isalpha():
            processed_words.append(word.lower())
    return processed_words
if __name__ == '__main__':
    sample_string = "Hello, World! This is a test sentence with various punctuation and numbers 123."
    result = extract_words(sample_string)
    print(result)