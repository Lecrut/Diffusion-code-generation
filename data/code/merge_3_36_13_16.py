def reverse_sentence(sentence: str) -> str:
    """Reverse a given sentence efficiently by slicing."""
    return sentence[::-1]

if __name__ == '__main__':
    # Sample input as per constraints (no user interaction, no command-line args)
    sample_input = "Hello World!"

    reversed_result = reverse_sentence(sample_input)
    
    print(reversed_result)