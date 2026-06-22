import string

def has_special_characters(text):
    special_chars = set(string.punctuation)
    stripped_text = ''.join(c for c in text if c not in special_chars)
    return len(text) != len(stripped_text)

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Hello@World!"
    result1 = has_special_characters(sample1)
    result2 = has_special_characters(sample2)
    print(result1)
    print(result2)