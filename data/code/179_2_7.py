def reverse_sentence(sentence: str) -> str:
    words = sentence.split()
    words.reverse()
    return " ".join(words)

if __name__ == '__main__':
    sample_sentence1 = "Hello world this is a test"
    result1 = reverse_sentence(sample_sentence1)
    print(f"Original: {sample_sentence1}")
    print(f"Reversed: {result1}")

    sample_sentence2 = "Python programming is fun"
    result2 = reverse_sentence(sample_sentence2)
    print(f"Original: {sample_sentence2}")
    print(f"Reversed: {result2}")

    sample_sentence3 = "Keep it simple"
    result3 = reverse_sentence(sample_sentence3)
    print(f"Original: {sample_sentence3}")
    print(f"Reversed: {result3}")