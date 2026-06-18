def combine_words(word1: str, word2: str) -> str:
    return f"{word1} {word2}"
if __name__ == '__main__':
    sample_word1 = "hello"
    sample_word2 = "world"
    result = combine_words(sample_word1, sample_word2)
    print(result)