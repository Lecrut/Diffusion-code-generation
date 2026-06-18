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
        if 'a' <= char <= 'z':  # Ensure only alphabetic characters are counted
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    
    # Collect letters that have a count greater than one
    repeated_letters = {letter for letter, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    sample_input_1 = "Hello World"
    sample_input_2 = "A man, a plan, a canal: Panama!"
    sample_input_3 = "Programming is fun!!"

    print("Sample 1:", find_repeated_letters(sample_input_1))
    print("Sample 2:", find_repeated_letters(sample_input_2))
    print("Sample 3:", find_repeated_letters(sample_input_3))