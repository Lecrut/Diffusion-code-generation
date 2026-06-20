import string

def has_special_characters(text):
    special_chars = set(string.punctuation)
    return any(char in special_chars for char in text)

if __name__ == '__main__':
    sample_string_1 = "Hello, World!"
    sample_string_2 = "Hello World"
    sample_string_3 = "NoPunctuation123"
    print(has_special_characters(sample_string_1))
    print(has_special_characters(sample_string_2))
    print(has_special_characters(sample_string_3))