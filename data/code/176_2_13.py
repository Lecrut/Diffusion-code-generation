import re

def tokenize_string(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_string = "This is a sample string with various words and punctuation! How about this?"
    try:
        tokens = tokenize_string(sample_string)
        print(tokens)
    except ValueError as e:
        print(e)