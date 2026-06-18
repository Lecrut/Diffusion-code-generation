def reverse_word(text: str) -> str:
    """
    Reverses a single word provided as input using Python's string slicing.
    
    This function assumes that 'text' is already an isolated word (without surrounding 
    whitespace). If the entire sentence or line was passed, it will simply be reversed,
    which satisfies the core requirement of reversing via slicing efficiently.

    Args:
        text (str): The input string representing a single word or sequence of characters to reverse.

    Returns:
        str: A new string with all characters in 'text' reversed.
    
    Performance Note: 
    Python's slice assignment uses an optimized C-level implementation, making this O(n) operation.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies
    sample_input = "hello"

    result = reverse_word(sample_input)

    print(f"Original: {sample_input}")
    print(f"Reversed: {result}")