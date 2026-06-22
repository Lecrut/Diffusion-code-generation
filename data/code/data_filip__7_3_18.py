import string

def has_special_chars(text):
    return any(char in string.punctuation for char in text)

if __name__ == '__main__':
    sample_texts = ["Hello World", "Hello! World", "No special chars", "Wait... what?"]
    for text in sample_texts:
        result = has_special_chars(text)
        print(f"{result} -> {text}")