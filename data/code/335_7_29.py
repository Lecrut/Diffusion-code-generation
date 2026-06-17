import re
def split_sentence(sentence: str) -> list[str]:
    words = sentence.split()
    if not words:
        return []
    result = [word for word in words]
    return result
if __name__ == '__main__':
    sample_sentence = "Hello, world! This is a test."
    output_words = split_sentence(sample_sentence)
    print(output_words)