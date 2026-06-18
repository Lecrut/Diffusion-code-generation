def reverse_sentence(sentence: str) -> str:
    """
    Reverses a given sentence using efficient string slicing.
    
    Args:
        sentence (str): The input sentence to be reversed.
        
    Returns:
        str: The reversed sentence.
    """
    return sentence[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    # No user prompts, sys.stdin, or argparse usage allowed
    
    sample_sentences = [
        "Hello World!",
        "Python is awesome.",
        "The quick brown fox jumps over the lazy dog."
    ]

    for sentence in sample_sentences:
        reversed_sentence = reverse_sentence(sentence)
        print(f"Original: {sentence}")
        print(f"Reversed: {reversed_sentence}\n")