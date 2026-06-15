import string
def extract_words(text):
    words = []
    for char in text:
        if char.isalpha() or char.isspace():
            words.append(char)
    return [word.lower() for word in words if word]
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence with various punctuation."
    result = extract_words(sample_string)
    print(result)