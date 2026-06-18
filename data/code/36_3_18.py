def reverse_sentence(sentence):
    """Reverses a given sentence."""
    return ' '.join(reversed(sentence.split()))

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or interactive prompts
    samples = [
        "Hello, world!",
        "Python programming is fun.",
        "The quick brown fox jumps over the lazy dog."
    ]

    for sample in samples:
        print(f"Original: {sample}")
        reversed_sentence = reverse_sentence(sample)
        print("Reversed:", reversed_sentence)