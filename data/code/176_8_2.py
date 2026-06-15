import re
def tokenize_string(text):
    tokens = re.findall(r'\b\w+\b', text)
    return tokens
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, how are you?"
    sample_string2 = "  leading spaces and multiple   spaces\tand punctuation... "
    sample_string3 = "Word1, Word2. Word3"
    tokens1 = tokenize_string(sample_string1)
    print(f"Input: '{sample_string1}'")
    print(f"Tokens: {tokens1}")
    print("-" * 20)
    tokens2 = tokenize_string(sample_string2)
    print(f"Input: '{sample_string2.replace('\n', ' ')}'")
    print(f"Tokens: {tokens2}")
    print("-" * 20)
    tokens3 = tokenize_string(sample_string3)
    print(f"Input: '{sample_string3}'")
    print(f"Tokens: {tokens3}")