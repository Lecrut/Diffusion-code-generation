def combine_words(s1: str, s2: str) -> str:
    return f"{s1}{s2}"
if __name__ == '__main__':
    word_a = "Hello"
    word_b = "World"
    result = combine_words(word_a, word_b)
    print(result)