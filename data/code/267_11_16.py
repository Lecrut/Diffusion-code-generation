def filter_long_words(words: list) -> list:
    return [word for word in words if len(word) > 4]

if __name__ == '__main__':
    sample_words = ["short", "programming", "longerword", "test"]
    result = filter_long_words(sample_words)
    print(result)