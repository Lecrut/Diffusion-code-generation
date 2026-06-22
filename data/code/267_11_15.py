def filter_long_words(words: list) -> list:
    long_words = [word for word in words if len(word) > 4]
    return long_words

if __name__ == '__main__':
    sample_words1 = ["short", "longerword", "test"]
    result1 = filter_long_words(sample_words1)
    print(result1)

    sample_words2 = ["programming", "short", "algorithm"]
    result2 = filter_long_words(sample_words2)
    print(result2)