import re

def tokenize_string(text):
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_string = "This is a sample string with various words and punctuation! How about this?"
    tokens = tokenize_string(sample_string)
    print(tokens)