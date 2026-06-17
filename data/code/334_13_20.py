def combine_words(word1: str, word2: str) -> str:
    return f"{word1}{'' if not (len(word1) > 0 and len(word2) > 0) else ' '} {word2}"
if __name__ == '__main__':
    result = combine_words("hello", "world")
    print(result)