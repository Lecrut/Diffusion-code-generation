import re

def tokenize_string(sentence: str) -> list[str]:
    words = re.split(r'\W+', sentence)
    return [word for word in words if word]

if __name__ == '__main__':
    sample_sentence = "Hello, world! This is a test. Sentence with numbers 123."
    result = tokenize_string(sample_sentence)
    print(result)