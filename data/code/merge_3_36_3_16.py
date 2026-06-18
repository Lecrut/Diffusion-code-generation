def reverse_sentence(sentence: str) -> str:
    """Reverses a given sentence character by character."""
    return sentence[::-1]

if __name__ == '__main__':
    # Sample input data to avoid interactive prompts, sys.stdin, or network access.
    sample_input = "Hello World!"

    # Reverse the sample input and print the result.
    reversed_result = reverse_sentence(sample_input)
    print(reversed_result)