def reverse_sentence(sentence: str) -> str:
    """Reverses a given sentence string."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies.
    sample_input = "Hello World"
    
    reversed_text = reverse_sentence(sample_input)
    
    print(reversed_text)