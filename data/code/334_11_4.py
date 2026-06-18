def combine_words(str1: str, str2: str) -> str:
    return f"{str1}{str2}"
if __name__ == '__main__':
    word_a = "Hello"
    word_b = "World"
    result = combine_words(word_a, word_b)
    print(result)