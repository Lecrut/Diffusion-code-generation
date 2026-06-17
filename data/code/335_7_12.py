import re
def extract_words(sentence: str) -> list[str]:
    words = sentence.split()
    return [word for word in words if len(word.strip()) > 0]
if __name__ == '__main__':
    sample_sentence = "Hello, World! This is a test."
    result = extract_words(sample_sentence)
    print(result)