import re

def extract_words(text):
    word_pattern = r'\b\w+\b'
    words = re.findall(word_pattern, text)
    return [word.lower() for word in words]

if __name__ == '__main__':
    sample_text = "Hello World! This is a Test string with numbers 123 and symbols @#$"
    result = extract_words(sample_text)
    print(result)