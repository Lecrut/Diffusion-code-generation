def extract_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum() or char.isspace())
    words = cleaned_text.split()
    return words

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test string with some - punctuation and numbers 123."
    print(extract_words(sample_string))