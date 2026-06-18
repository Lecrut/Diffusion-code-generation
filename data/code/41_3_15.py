def process_string(s: str) -> tuple[str, str, str]:
    """
    Returns a tuple containing:
        1. The original string.
        2. The lowercase version of the string.
        3. A new string with all characters' cases swapped (uppercase becomes lowercase and vice versa).

    Parameters:
        s (str): The input string to process.

    Returns:
        tuple[str, str, str]: 
            - Original string
            - Lowercase version
            - Reversed case version
    """
    original = s
    lowercased = s.lower()
    
    # Swap cases using the swapcase method which is a built-in string method
    reversed_case = s.swapcase()

    return (original, lowercased, reversed_case)

if __name__ == '__main__':
    sample_string = "Hello World!"
    result_tuple = process_string(sample_string)
    
    # Print results for verification without user input prompts
    print(f"Original: {result_tuple[0]}")
    print(f"Lowercase: {result_tuple[1]}")
    print(f"Reversed Case: {result_tuple[2]}")