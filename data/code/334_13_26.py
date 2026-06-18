def combine_words(word1: str, word2: str) -> str:
    return f"{word1} {word2}" if (len(word1) > 0 or len(word2) > 0) else ""
if __name__ == '__main__':
    result = combine_words("Hello", "")
    print(result, end="")