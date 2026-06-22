import string

def isolate_punctuation(text):
    return ''.join(' ' if char in string.punctuation else char for char in text)

if __name__ == '__main__':
    sample_text = "Hello, world! How are you?"
    print(isolate_punctuation(sample_text))