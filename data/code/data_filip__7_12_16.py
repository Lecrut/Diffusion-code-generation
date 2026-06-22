import string

def has_punctuation(text):
    for char in text:
        if char in string.punctuation:
            return True
    return False

if __name__ == '__main__':
    sample_strings = ["Hello, world!", "No symbols here", "Test@123", "Plain text"]
    for s in sample_strings:
        print(f"String: '{s}' contains punctuation: {has_punctuation(s)}")