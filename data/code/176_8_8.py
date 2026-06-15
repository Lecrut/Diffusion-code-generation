import re
def tokenize_string(text):
    tokens = re.findall(r'\b\w+\b', text)
    return tokens
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, how are you?"
    sample_string2 = "  multiple   spaces   and , punctuation! "
    sample_string3 = "Word1-Word2. Word3? End."
    tokens1 = tokenize_string(sample_string1)
    print(f"Input: '{sample_string1}'")
    print(f"Tokens: {tokens1}")
    tokens2 = tokenize_string(sample_string2)
    print(f"Input: '{sample_string2}'")
    print(f"Tokens: {tokens2}")
    tokens3 = tokenize_string(sample_string3)
    print(f"Input: '{sample_string3}'")
    print(f"Tokens: {tokens3}")