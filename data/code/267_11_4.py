def is_word_long(word: str, threshold: int) -> bool:
    return len(word) > threshold
if __name__ == '__main__':
    word1 = "programming"
    threshold1 = 7
    result1 = is_word_long(word1, threshold1)
    print(f"{word1} > {threshold1}: {result1}")
    word2 = "short"
    threshold2 = 5
    result2 = is_word_long(word2, threshold2)
    print(f"{word2} > {threshold2}: {result2}")
    word3 = "efficiency"
    threshold3 = 10
    result3 = is_word_long(word3, threshold3)
    print(f"{word3} > {threshold3}: {result3}")