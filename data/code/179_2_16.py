def reverse_words(sentence: str) -> str:
    words = sentence.split()
    reversed_words = list(reversed(words))
    return " ".join(reversed_words)

if __name__ == '__main__':
    sample_sentence1 = "Hello world this is a test"
    result1 = reverse_words(sample_sentence1)
    print(f"Original: {sample_sentence1}")
    print(f"Reversed: {result1}")

    sample_sentence2 = "Python programming is fun"
    result2 = reverse_words(sample_sentence2)
    print(f"Original: {sample_sentence2}")
    print(f"Reversed: {result2}")