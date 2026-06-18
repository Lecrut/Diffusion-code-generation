def reverse_sentence(sentence: str) -> str:
    """Reverses a given sentence character by character."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies.
    sample_sentences = [
        "Hello, World!",
        "Python is awesome.",
        "The quick brown fox."
    ]

    for test_sentence in sample_sentences:
        reversed_text = reverse_sentence(test_sentence)
        print(f"Original: {test_sentence}")
        print(f"Reversed:{reversed_text}\n")