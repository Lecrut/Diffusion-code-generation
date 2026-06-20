import re

def extract_words(text):
    return re.findall(r'\w+', text)

if __name__ == '__main__':
    sample_input = """
    Hello, world!
    This is a test-string with numbers 123 and symbols @#.
    Another line with Python3.9.
    """
    result = extract_words(sample_input)
    print(result)