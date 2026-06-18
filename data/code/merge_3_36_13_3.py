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
    sample_sentences = [
        "Hello, World!",
        "Python is awesome.",
        "The quick brown fox jumps over the lazy dog."
    ]

    for s in sample_sentences:
        reversed_s = reverse_sentence(s)
        print(f"Original: {s}")
        print(f"Reversed: {reversed_s}\n")