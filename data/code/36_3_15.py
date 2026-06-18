def reverse_sentence(sentence: str) -> str:
    """Reverses a given sentence."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    test_sentences = [
        "Hello, World!",
        "Python is awesome.",
        "The quick brown fox jumps over the lazy dog."
    ]

    for sentence in test_sentences:
        reversed_sentence = reverse_sentence(sentence)
        print(reversed_sentence)