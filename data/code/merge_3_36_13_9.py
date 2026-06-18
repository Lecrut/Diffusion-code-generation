def reverse_string(s: str) -> str:
    """Reverses a given string efficiently using slicing."""
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample sentence to satisfy requirements without user input or prompts.
    sample_sentence = "Hello, World!"

    reversed_result = reverse_string(sample_sentence)
    
    print("Original:", end=" ")
    print(reversed_result)