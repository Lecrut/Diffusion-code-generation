import re
def tokenize_string(text):
    tokens = re.findall(r'\b\w+\b', text)
    return tokens
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, how are you?"
    sample_string2 = "  Multiple   spaces \t and punctuation... end."
    sample_string3 = "Word1,Word2.Word3"
    result1 = tokenize_string(sample_string1)
    print(f"Input: '{sample_string1}'")
    print(f"Output: {result1}")
    result2 = tokenize_string(sample_string2)
    print(f"Input: '{sample_string2}'")
    print(f"Output: {result2}")
    result3 = tokenize_string(sample_string3)
    print(f"Input: '{sample_string3}'")
    print(f"Output: {result3}")