import string

def has_special_characters(text):
    special_chars = set(string.punctuation)
    for char in text:
        if char in special_chars:
            return True
    return False

if __name__ == '__main__':
    sample_text_1 = "Hello, World!"
    sample_text_2 = "NoSpecialCharsHere"
    sample_text_3 = "Test@123#Code"
    
    print(has_special_characters(sample_text_1))
    print(has_special_characters(sample_text_2))
    print(has_special_characters(sample_text_3))