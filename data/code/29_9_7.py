def reverse_word(word: str) -> str:
    """
    Reverses a single word using Python's string slicing capabilities.
    
    Args:
        word (str): The input word to be reversed.
        
    Returns:
        str: The reversed version of the input word.
    """
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    samples = ["hello", "Python", "optimized"]
    
    print("Original Word | Reversed Word")
    print("-" * 30)
    
    for word in samples:
        reversed_word = reverse_word(word)
        print(f"{word:<15} | {reversed_word}")