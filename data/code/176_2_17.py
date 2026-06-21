import re

def tokenize_string(text):
    return re.findall(r'\b\w+\b', text)

if __name__ == '__main__':
    sample_string = "This is another example string with words and punctuation! Let's see how it works."
    tokens = tokenize_string(sample_string)
    print(tokens)