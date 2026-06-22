import string

def isolate_punctuation(text):
    punctuation_chars = set(string.punctuation)
    return [char for char in text if char in punctuation_chars]

if __name__ == '__main__':
    sample_text = "Hello, world! How are you?"
    isolated_punctuation = isolate_punctuation(sample_text)
    print(isolated_punctuation)