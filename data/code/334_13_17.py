def combine_words(word1: str, word2: str) -> str:
    return f"{word1} {word2}" if any([len(word1), len(word2)]) else ""
if __name__ == '__main__':
    print(combine_words("Hello", "World"))