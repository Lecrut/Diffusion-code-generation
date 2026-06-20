import re

def has_special_characters(text):
    return any(not c.isalnum() and not c.isspace() for c in text)

if __name__ == '__main__':
    sample_texts = [
        "Hello World",
        "Hello@World!",
        "12345",
        "Special#Chars$Here"
    ]

    for text in sample_texts:
        result = has_special_characters(text)
        print(result)