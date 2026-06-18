def combine_words(word1: str, word2: str) -> str:
    return f"{word1} and {word2}"
if __name__ == '__main__':
    result = combine_words("Hello", "")
    print(result)