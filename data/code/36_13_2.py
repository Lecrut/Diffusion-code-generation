def reverse_sentence(sentence: str) -> str:
    """Reverses a given sentence efficiently using string slicing."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the program runs without user input.
    test_sentences = [
        "Hello, World!",
        "Python is awesome.",
        ""
    ]

    for s in test_sentences:
        reversed_s = reverse_sentence(s)
        print(f"Original: {s}")
        print(f"Reversed: {reversed_s}\n")