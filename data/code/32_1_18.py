def calculate_phrase_length(phrase: str) -> int:
    """
    Calculates the total character count of a given string phrase using 
    Python's optimized built-in len() function.
    
    Args:
        phrase (str): The input string to measure length for.
        
    Returns:
        int: Total number of characters in the phrase.
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values with no user input or network access required
    samples = [
        "Hello, World!",
        "",
        "Python is amazing.",
        "x" * 10**6  # Large string test for performance validation
    ]

    print("Character length calculations:")
    for sample in samples:
        calculated_length = calculate_phrase_length(sample)
        print(f"'{sample[:20]}...' if len(sample)>20 else '{sample}': Length is {calculated_length}")