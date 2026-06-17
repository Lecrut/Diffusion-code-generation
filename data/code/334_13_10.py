def combine_words(word1: str, word2: str) -> str:
    if not isinstance(word1, str):
        raise TypeError("First argument must be a string.")
    if not isinstance(word2, str):
        raise TypeError("Second argument must be a string.")
    result = f"{word1} {word2}"
    return result
if __name__ == '__main__':
    word_a: str = ""
    word_b: str = "hello"
    output_str: str = combine_words(word_a, word_b)
    print(output_str.strip())