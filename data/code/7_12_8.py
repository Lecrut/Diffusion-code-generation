import string

def contains_punctuation(text):
    for char in text:
        if char in string.punctuation:
            return True
    return False

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "Wait, really?",
        "Price: $19.99",
        "NoSymbolsHere",
        "Special!@#$%",
        "Just letters and numbers"
    ]
    for s in sample_strings:
        print(contains_punctuation(s))