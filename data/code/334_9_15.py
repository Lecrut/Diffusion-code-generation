def combine_words(word1: str, word2: str) -> str:
    return f"{word1}{word2}"
if __name__ == '__main__':
    word_a = "Hello"
    word_b = "World"
    result = combine_words(word_a, word_b)
    print(result)