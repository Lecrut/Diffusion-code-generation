def main():
    """
    Reverses a given sentence without using interactive input prompts.
    This function demonstrates the logic by processing hard-coded sample values.
    It does not call input(), sys.stdin, or require command-line arguments.
    """
    
    # Hard-coded sample sentences to avoid user interaction requirements
    samples = [
        "Hello World",
        "Python Programming is Fun"
    ]

    for sentence in samples:
        reversed_sentence = sentence[::-1]
        print(f"Original: {sentence}")
        print(f"Reversed: {reversed_sentence}\n")

if __name__ == '__main__':
    main()