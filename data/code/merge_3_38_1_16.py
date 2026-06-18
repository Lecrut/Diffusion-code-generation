def find_repeated_letters(text: str) -> set:
    """
    Returns a set of all letters that appear more than once in the input string.
    
    The function is case-insensitive and ignores non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        set: A set containing unique repeated letters found in the string.
    """
    letter_counts = {}
    
    # Iterate over each character, converting to lowercase for case-insensitivity
    for char in text.lower():
        if 'a' <= char <= 'z':  # Check if it's an alphabetic character
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    
    # Collect letters that have a count greater than 1
    repeated_letters = {letter for letter, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    sample_input = "Hello World! This is an example of finding repeated letters."
    result = find_repeated_letters(sample_input)
    print(f"Repeated letters: {sorted(result)}")

    # Additional test case with different characters and casing
    sample_input_2 = "AaBbCc123!!"
    result_2 = find_repeated_letters(sample_input_2)
    print(f"Repeated letters (test 2): {sorted(result_2)}")