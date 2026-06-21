import re

def tokenize_text(text):
    tokens = re.findall(r'\b\w+\b', text.lower())
    return list(dict.fromkeys(tokens))

if __name__ == '__main__':
    sample_text = "Hello, world! Hello, everyone."
    print(tokenize_text(sample_text))