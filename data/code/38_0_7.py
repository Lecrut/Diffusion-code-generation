def find_repeated_letters(text: str) -> set:
    """
    Finds all letters in the input string that appear more than once.
    The check is case-insensitive (e.g., 'A' and 'a' are considered the same letter).
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        set: A set of unique letters found multiple times in lowercase format.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    letter_counts = {}
    
    # Iterate over each character that is an alphabetic letter
    for char in text:
        if 'a' <= char.lower() <= 'z':  # Check only ASCII lowercase letters range to ensure it's a letter
            lower_char = char.lower()
            
            if lower_char not in letter_counts:
                letter_counts[lower_char] = 0
                
            letter_counts[lower_char] += 1
            
    # Identify which counts are greater than 1 and collect them into the result set
    repeated_letters = {letter for letter, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required.
    test_cases = [
        "Hello World",
        "Python Programming",
        "AaBbCcDd",
        "NoRepeatsHere123!",
        "The quick brown fox jumps over the lazy dog"
    ]

    for text in test_cases:
        repeated_letters_set = find_repeated_letters(text)
        
        if not repeated_letters_set:
            print(f"No repeated letters found in '{text}'.")
        else:
            # Convert set to a sorted list of strings for cleaner output representation
            result_list = [f"'{char}'" for char in sorted(repeated_letters_set)]
            printed_result = ", ".join(result_list)
            print(f"In '{text}': Repeated letters are {printed_result}.")