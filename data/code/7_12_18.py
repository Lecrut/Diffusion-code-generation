import string

def contains_punctuation(text: str) -> bool:
    return any(char in string.punctuation for char in text)

if __name__ == '__main__':
    sample_text = "Hello, world!"
    result = contains_punctuation(sample_text)
    print(result)