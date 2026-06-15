import string
def extract_words(text):
    words = []
    for char in text:
        if char.isalnum():
            words.append(char)
    return [word.lower() for word in words]
if __name__ == '__main__':
    sample_string = "Hello, world! This is a test sentence with 123 numbers."
    result = extract_words(sample_string)
    print(result)