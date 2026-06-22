def filter_long_words(words: list) -> list:
    if not all(isinstance(word, str) for word in words):
        raise ValueError("All elements in the input list must be strings.")
    return [word for word in words if len(word) > 4]

if __name__ == '__main__':
    sample_words = ["hello", "world", "tiny", "example", "list", "of", "words"]
    long_words = filter_long_words(sample_words)
    print(long_words)