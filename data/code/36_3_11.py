def reverse_sentence(sentence: str) -> str:
    """Reverses a given sentence character by character."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    samples = [
        "Hello, World!",
        "Python is awesome.",
        "The quick brown fox jumps over the lazy dog."
    ]

    for text in samples:
        reversed_text = reverse_sentence(text)
        print(f"Original: {text}")
        print(f"Reversed: {reversed_text}\n")