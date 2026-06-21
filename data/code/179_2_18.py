def reverse_words_in_sentence(sentence: str) -> str:
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string.")
    
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

if __name__ == '__main__':
    sample_sentence1 = "Hello world this is a test"
    result1 = reverse_words_in_sentence(sample_sentence1)
    print(f"Original: {sample_sentence1}")
    print(f"Reversed: {result1}")

    sample_sentence2 = "Optimization is key"
    result2 = reverse_words_in_sentence(sample_sentence2)
    print(f"Original: {sample_sentence2}")
    print(f"Reversed: {result2}")

    sample_sentence3 = "a single word"
    result3 = reverse_words_in_sentence(sample_sentence3)
    print(f"Original: {sample_sentence3}")
    print(f"Reversed: {result3}")