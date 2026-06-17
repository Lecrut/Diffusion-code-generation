def combine_words(word1: str, word2: str) -> str:
    return f"{word1} {word2}"
if __name__ == '__main__':
    sample_word_1 = "Python"
    sample_word_2 = "Programming"
    result = combine_words(sample_word_1, sample_word_2)
    print(result)