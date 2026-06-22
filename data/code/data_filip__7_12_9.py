import string

def has_punctuation(text: str) -> bool:
    return any(char in string.punctuation for char in text)

if __name__ == '__main__':
    sample_text = "Hello, World!"
    result = has_punctuation(sample_text)
    print(result)