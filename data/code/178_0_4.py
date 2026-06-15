import string
def extract_words(text):
    words = []
    for char in text:
        if char.isalpha() or char.isspace():
            if char.isalpha():
                words.append(char.lower())
    return words
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence with various punctuation."
    result = extract_words(sample_string)
    print(result)