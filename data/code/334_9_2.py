def combine_words(word1: str, word2: str) -> str:
    return f"{word1}{word2}"
if __name__ == '__main__':
    sample_word_1 = "Hello"
    sample_word_2 = "World"
    result = combine_words(sample_word_1, sample_word_2)
    print(result)