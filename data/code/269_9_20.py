import re

def extract_punctuation(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    
    punctuation_marks = re.findall(r'[^\w\s]', text)
    return [mark for mark in punctuation_marks if not re.search(r'\b', mark)]

if __name__ == '__main__':
    sample_string = "Hello, world! How are you? This is a test."
    result = extract_punctuation(sample_string)
    print(result)