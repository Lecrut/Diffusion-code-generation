def split_sentence(sentence: str) -> list[str]:
    cleaned = sentence.strip()
    return cleaned.split()
if __name__ == '__main__':
    sample_sentence = "  Hello, World! This is an example. Pythonic code here."
    result_words = split_sentence(sample_sentence)
    print(result_words)