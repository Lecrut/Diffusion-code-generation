import re

def tokenize_and_filter(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_string = "This is a sample string with various words and punctuation! How about this?"
    try:
        words = tokenize_and_filter(sample_string)
        print(words)
    except ValueError as e:
        print(e)