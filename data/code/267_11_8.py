def filter_long_words(words: list) -> list:
    return [word for word in words if len(word) > 4]

if __name__ == '__main__':
    sample_words = ["programming", "short", "algorithm", "data", "science"]
    long_words = filter_long_words(sample_words)
    print(long_words)