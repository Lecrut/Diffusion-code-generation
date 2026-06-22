import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

if __name__ == '__main__':
    sample_text = "Hello, world! How are you?"
    print(remove_punctuation(sample_text))