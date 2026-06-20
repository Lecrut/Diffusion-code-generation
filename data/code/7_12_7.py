import string

def has_punctuation(s):
    return any(char in string.punctuation for char in s)

if __name__ == '__main__':
    samples = ["hello world", "hello, world!", "no punctuation here", "what's up?", "1234567890"]
    for sample in samples:
        print(has_punctuation(sample))