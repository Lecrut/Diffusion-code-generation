import sys
def combine_words(word1: str, word2: str) -> None:
    combined = f"{word1} {word2}"
    print(combined)
if __name__ == '__main__':
    sample_word_1 = "hello"
    sample_word_2 = "world"
    try:
        combine_words(sample_word_1, sample_word_2)
        sys.exit(0)
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)