def split_sentence(sentence: str) -> list[str]:
    return [word.strip() for word in sentence.split()]
if __name__ == '__main__':
    sample_sentence = "  Hello, World! How are you doing today?  "
    words = split_sentence(sample_sentence)
    print(words)