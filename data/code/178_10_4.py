import re

def extract_words(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = re.findall(r'\b\w+\b', text)
    return words

if __name__ == '__main__':
    sample_string = "Hello world! This is a test, how are you doing today? Python programming is fun."
    extracted_words = extract_words(sample_string)
    print(extracted_words)