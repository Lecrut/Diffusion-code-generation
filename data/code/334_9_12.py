def combine_words(word1: str, word2: str) -> str:
    return f"{word1}{word2}"
if __name__ == '__main__':
    word_1 = "Hello"
    word_2 = "World"
    result = combine_words(word_1, word_2)
    print(result)