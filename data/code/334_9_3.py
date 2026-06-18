def combine_words(word1: str, word2: str) -> str:
    return f"{word1}{word2}"
if __name__ == '__main__':
    sample_word1 = "Hello"
    sample_word2 = "World"
    result = combine_words(sample_word1, sample_word2)
    print(result)