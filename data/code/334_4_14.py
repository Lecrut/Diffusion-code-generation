import sys
def combine_words(word1: str, word2: str) -> None:
    result = f"{word1} {word2}"
    print(result)
if __name__ == '__main__':
    sample_word1 = "hello"
    sample_word2 = "world"
    try:
        combine_words(sample_word1, sample_word2)
    except Exception as e:
        sys.exit(1)
sys.exit(0)