import re
def tokenize_string(text):
    tokens = re.findall(r'\b\w+\b', text)
    return tokens
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, how are you?"
    sample_string2 = "  leading spaces and multiple   spaces   between words.  Punctuation like commas and periods."
    sample_string3 = "Word1, Word2.Word3"
    sample_string4 = "  a b c d e "
    tokens1 = tokenize_string(sample_string1)
    print(f"Input: '{sample_string1}'")
    print(f"Tokens: {tokens1}\n")
    tokens2 = tokenize_string(sample_string2)
    print(f"Input: '{sample_string2}'")
    print(f"Tokens: {tokens2}\n")
    tokens3 = tokenize_string(sample_string3)
    print(f"Input: '{sample_string3}'")
    print(f"Tokens: {tokens3}\n")
    tokens4 = tokenize_string(sample_string4)
    print(f"Input: '{sample_string4}'")
    print(f"Tokens: {tokens4}\n")