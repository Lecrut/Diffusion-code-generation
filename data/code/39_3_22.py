import re

def extract_words(text):
    return re.findall(r'\w+', text)

if __name__ == '__main__':
    sample = "Hello world!\nThis is a test.\n123 numbers 456."
    result = extract_words(sample)
    print(result)