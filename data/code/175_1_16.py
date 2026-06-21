import re

TOKEN_PATTERN = re.compile(r'\b\w+\b')

def split_alphanumeric(sentence: str) -> list[str]:
    return TOKEN_PATTERN.findall(sentence)

if __name__ == '__main__':
    sample_sentence = "Hello world! This is a test sentence, 123."
    result = split_alphanumeric(sample_sentence)
    print(result)