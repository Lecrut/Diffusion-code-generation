import string

def has_punctuation(text):
    for char in text:
        if char in string.punctuation:
            return True
    return False

if __name__ == '__main__':
    sample1 = "Hello, world!"
    sample2 = "NoSpecialCharsHere"
    sample3 = "Price: $100.00"
    
    print(has_punctuation(sample1))
    print(has_punctuation(sample2))
    print(has_punctuation(sample3))