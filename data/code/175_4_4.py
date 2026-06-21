import re

def find_words():
    text = "Hello, world! This is a test."
    words = re.findall(r'\b\w+\b', text)
    return words

if __name__ == '__main__':
    print(find_words())