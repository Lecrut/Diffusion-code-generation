def reverse_sentence(sentence: str) -> str:
    """
    Reverses a given sentence efficiently using string slicing.
    
    Args:
        sentence (str): The input sentence to be reversed.
        
    Returns:
        str: The reversed sentence.
    """
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    # No user interaction, command-line arguments, or network access is used here.
    
    test_sentences = [
        "Hello World",
        "Python Programming",
        "The quick brown fox jumps over the lazy dog"
    ]

    for sentence in test_sentences:
        reversed_sentence = reverse_sentence(sentence)
        print(f"Original: {sentence}")
        print(f"Reversed: {reversed_sentence}\n")