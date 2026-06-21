import re

TOKEN_PATTERN = re.compile(r'\W+')

def tokenize_alphanumeric(sentence: str) -> list[str]:
    return TOKEN_PATTERN.split(sentence)

if __name__ == '__main__':
    sample_sentence = "Hello world! This is a test sentence, 123."
    result = tokenize_alphanumeric(sample_sentence)
    print(result)