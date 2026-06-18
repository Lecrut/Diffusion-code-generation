def reverse_sentence(sentence):
    """Reverses a given sentence."""
    return " ".join(reversed(sentence.split()))

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or network access.
    samples = [
        "Hello, world!",
        "Python is great.",
        "The quick brown fox jumps."
    ]

    for sample in samples:
        reversed_text = reverse_sentence(sample)
        print(f"Original: {sample}")
        print(f"Reversed: {reversed_text}\n")