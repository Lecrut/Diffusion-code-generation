import string

PUNCTUATION_CHARS = set(string.punctuation)

def isolate_punctuation(text):
    return [char for char in text if char in PUNCTUATION_CHARS]

if __name__ == '__main__':
    sample_text = "Hello, world! How are you?"
    print(isolate_punctuation(sample_text))