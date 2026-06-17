def combine_words(word1: str, word2: str) -> str:
    return f"{word1} {word2}" if (word1 and word2) else ""
if __name__ == '__main__':
    result = combine_words("Hello", "World")
    print(result)