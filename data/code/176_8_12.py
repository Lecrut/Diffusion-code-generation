import re

def replace_non_word_with_space(text):
    return re.sub(r'\W+', ' ', text)

def tokenize_string(text):
    text = replace_non_word_with_space(text)
    tokens = text.split()
    return tokens

if __name__ == '__main__':
    sample_string = "Hello, world! This is a test, how are you doing? 123."
    print(f"Input: '{sample_string}'")
    print(f"Tokens: {tokenize_string(sample_string)}\n")