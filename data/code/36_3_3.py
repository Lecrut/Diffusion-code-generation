def main():
    """
    Reverses a sentence without user interaction by using hard-coded sample values.
    This function demonstrates the reversal logic directly without prompting or input().
    """
    # Hard-coded sample sentences to demonstrate functionality
    samples = [
        "Hello, World!",
        "Python is awesome.",
        "The quick brown fox jumps over the lazy dog."
    ]

    for sentence in samples:
        reversed_sentence = sentence[::-1]
        print(reversed_sentence)

if __name__ == '__main__':
    main()