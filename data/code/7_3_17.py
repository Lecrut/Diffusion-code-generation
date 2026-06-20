import string

def has_special_chars(text):
    specials = set(string.punctuation)
    return any(char in specials for char in text)

if __name__ == '__main__':
    sample_text = "Hello World!@#"
    result = has_special_chars(sample_text)
    print(result)