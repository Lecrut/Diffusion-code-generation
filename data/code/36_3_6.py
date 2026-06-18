def reverse_sentence(sentence: str) -> str:
    """Reverses a given sentence character by character."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    test_sentences = [
        "Hello, World!",
        "Python is awesome.",
        "",  # Edge case: empty string
        "A man a plan a canal Panama",
    ]

    for sentence in test_sentences:
        reversed_sentence = reverse_sentence(sentence)
        print(f"Original: {sentence}")
        print(f"Reversed: {reversed_sentence}\n")