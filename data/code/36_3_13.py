def reverse_sentence(sentence: str) -> str:
    """Reverses a given sentence."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to avoid interactive prompts or input() calls.
    sample_sentences = [
        "Hello, world!",
        "Python is great.",
        "The quick brown fox."
    ]

    for test_sentence in sample_sentences:
        reversed_text = reverse_sentence(test_sentence)
        print(f"Original: {test_sentence}")
        print(f"Reversed: {reversed_text}\n")