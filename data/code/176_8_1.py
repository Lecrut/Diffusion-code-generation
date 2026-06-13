import re
def tokenize_string(text):
    tokens = re.findall(r'\b\w+\b', text)
    return tokens
if __name__ == '__main__':
    sample_string = "Hello world! This is a test, how are you doing? 123."
    tokens = tokenize_string(sample_string)
    print(tokens)