import re
def tokenize_string(text):
    tokens = re.findall(r'\b\w+\b', text)
    return tokens
if __name__ == '__main__':
    sample_string1 = "Hello world! This is a test, how are you?"
    sample_string2 = "  leading spaces and   multiple    spaces \t and punctuation."
    sample_string3 = "Word1,Word2.Word3"
    sample_string4 = "   \n\t  "
    result1 = tokenize_string(sample_string1)
    result2 = tokenize_string(sample_string2)
    result3 = tokenize_string(sample_string3)
    result4 = tokenize_string(sample_string4)
    print(f"Input: '{sample_string1}'")
    print(f"Output: {result1}\n")
    print(f"Input: '{sample_string2}'")
    print(f"Output: {result2}\n")
    print(f"Input: '{sample_string3}'")
    print(f"Output: {result3}\n")
    print(f"Input: '{sample_string4}'")
    print(f"Output: {result4}\n")