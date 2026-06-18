def reverse_sentence(sentence: str) -> str:
    """Returns a new string with characters in reversed order."""
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the program runs without user input, 
    # command-line arguments, or network access.
    sample_input = "Hello World!"

    display_text = f"Original Sentence: {sample_input}\nReversed Sentence: {reverse_sentence(sample_input)}"
    
    print(display_text)