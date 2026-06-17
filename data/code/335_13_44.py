def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello, world! This is an example of efficient string processing."
    words = split_sentence(sample_sentence)
    print("Words extracted:", words)
    assert isinstance(words, list), "Output must be a list"
    assert len(words) > 0, "Input sentence should contain at least one word"