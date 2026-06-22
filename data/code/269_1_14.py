import string

def remove_punctuation(text):
    return ''.join(char for char in text if char not in string.punctuation)

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test."
    print(remove_punctuation(sample_text))