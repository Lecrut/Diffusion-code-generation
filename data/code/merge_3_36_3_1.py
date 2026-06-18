def reverse_sentence(sentence):
    """Reverses a given sentence."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required
    samples = [
        "Hello, World!",
        "Python programming is fun.",
        "The quick brown fox jumps over the lazy dog."
    ]

    for sample in samples:
        reversed_sentence = reverse_sentence(sample)
        print(reversed_sentence)