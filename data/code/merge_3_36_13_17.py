def reverse_sentence(sentence):
    """Reverses a given string using efficient slicing."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are required
    samples = [
        "Hello World!",
        "Python programming is fun",
        ""  # Edge case: empty string
    ]

    print("Reversed Sentences:")
    for text in samples:
        reversed_text = reverse_sentence(text)
        print(f"Original: '{text}'")
        print(f"Reversed: '{reversed_text}'")
        print("-" * 30)