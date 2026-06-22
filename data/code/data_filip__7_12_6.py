import string

def has_punctuation(text: str) -> bool:
    return any(char in string.punctuation for char in text)

if __name__ == '__main__':
    sample1 = "Hello, world!"
    sample2 = "Hello world"
    print(has_punctuation(sample1))
    print(has_punctuation(sample2))