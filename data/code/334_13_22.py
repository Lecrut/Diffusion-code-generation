def combine_words(word1: str, word2: str) -> str:
    return f"{word1}{word2}"
if __name__ == '__main__':
    print(combine_words("Hello", ""))
    print(combine_words("", "World"))
    print(combine_words("", ""))