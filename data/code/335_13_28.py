def split_sentence(sentence: str) -> list[str]:
    return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello, world! This is a test."
    result_words = split_sentence(sample_sentence)
    assert isinstance(result_words, list), "Result must be a list"
    for word in result_words:
        if not isinstance(word, str):
            raise TypeError("All elements in the returned list must be strings")