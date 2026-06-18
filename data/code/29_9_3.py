def reverse_word(word: str) -> str:
    """
    Reverses a single word using Python's string slicing capability.
    
    Args:
        word (str): The input word to be reversed.
        
    Returns:
        str: The reversed version of the input word.
    """
    return word[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user interaction or file I/O
    test_words = ["hello", "Python3", "optimized"]
    
    print("Reversing words using slicing:")
    reversed_results = [reverse_word(word) for word in test_words]
    
    for original, reversed_val in zip(test_words, reversed_results):
        print(f"Original: '{original}' -> Reversed: '{reversed_val}'")