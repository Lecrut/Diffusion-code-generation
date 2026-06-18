def combine_words(word1: str, word2: str) -> str:
    return f"{word1}{word2}"
if __name__ == '__main__':
    print(combine_words("Hello", "World"))
    assert combine_words("", "") == ""
    assert combine_words("", "Test") == "Test"
    assert combine_words("Prefix", "") == "Prefix"