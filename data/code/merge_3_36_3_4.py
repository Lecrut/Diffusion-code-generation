def reverse_sentence(sentence: str) -> str:
    """Returns the reversed version of the input sentence."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies
    sample_sentences = [
        "Hello, World!",
        "Python is awesome.",
        "The quick brown fox jumps over the lazy dog."
    ]

    for sentence in sample_sentences:
        reversed_sentence = reverse_sentence(sentence)
        print(f"Original: {sentence}")
        print(f"Reversed: {reversed_sentence}\n")