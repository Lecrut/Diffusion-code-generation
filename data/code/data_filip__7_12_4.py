import string

def has_punctuation(text):
    for char in text:
        if char in string.punctuation:
            return True
    return False

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Hello, World!",
        "No punctuation here",
        "Special chars: @#$%",
        "Just text"
    ]
    for s in sample_strings:
        result = has_punctuation(s)
        print(f"{s}: {result}")