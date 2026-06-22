import re

def replace_whitespace_with_underscores(text):
    return re.sub(r'\s', '_', text)

if __name__ == '__main__':
    sample_input = "Hello World 123"
    result = replace_whitespace_with_underscores(sample_input)
    print(result)