import string

def contains_punctuation(text: str) -> bool:
    return any(char in string.punctuation for char in text)

if __name__ == '__main__':
    sample_texts = ["Hello, World!", "No punctuation here", "Wait... really?"]
    for text in sample_texts:
        result = contains_punctuation(text)
        print(f"{text}: {result}")