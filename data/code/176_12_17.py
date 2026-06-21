def is_valid_text(text):
    return isinstance(text, str)

def find_alphabetic_words(text):
    if not is_valid_text(text):
        raise ValueError("Input must be a string")
    
    words = [word for word in text.split() if word.isalpha()]
    return words

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test."
    alphabetic_words = find_alphabetic_words(sample_text)
    print(alphabetic_words)