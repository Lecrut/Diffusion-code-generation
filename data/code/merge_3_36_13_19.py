def reverse_sentence(sentence: str) -> str:
    """Reverse a given sentence using string slicing."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the program runs without user input
    sample_sentences = [
        "Hello, World!",
        "Python is awesome.",
        "The quick brown fox jumps over the lazy dog."
    ]

    for sentence in sample_sentences:
        reversed_sentence = reverse_sentence(sentence)
        print(f"Original: {sentence}")
        print(f"Reversed: {reversed_sentence}\n")