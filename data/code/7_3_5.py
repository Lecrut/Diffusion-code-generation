import string

def contains_special_chars(text):
    special_chars = set(string.punctuation)
    return any(char in special_chars for char in text)

if __name__ == '__main__':
    sample_text = "Hello, World!"
    result = contains_special_chars(sample_text)
    print(result)