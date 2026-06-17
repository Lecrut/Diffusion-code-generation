def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello, world! This is an example of efficient string splitting."
    words = split_sentence(sample_sentence)
    print(f"Input: {sample_sentence}")
    print(f"Output ({len(words)} words): {' '.join(words)}")