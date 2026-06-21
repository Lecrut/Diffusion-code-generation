import re

def process_sentence(sentence):
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', sentence)
    words = re.findall(r'\b\w+\b', cleaned.lower())
    return words

if __name__ == '__main__':
    sample_sentence = "Hello, this is a test sentence with various characters and numbers like 123!"
    result = process_sentence(sample_sentence)
    print(result)