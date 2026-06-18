def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters that appear more than once in the given sentence.
    Uses a dictionary to count letter occurrences efficiently, ignoring case and non-letter characters.

    Args:
        sentence (str): The input string to analyze.

    Returns:
        set: A set of lowercase letters found multiple times in the sentence.
    """
    char_count = {}
    
    # Iterate through each character in the sentence
    for char in sentence:
        if char.isalpha():  # Ensure only alphabetic characters are counted
            lower_char = char.lower()
            
            # Increment count if letter already exists, else initialize to 0 then increment
            char_count[lower_char] = char_count.get(lower_char, 0) + 1
            
    # Extract letters with a frequency greater than 1
    repeated_letters = {letter for letter, count in char_count.items() if count > 1}

    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample sentence to ensure the script runs without user input or external dependencies.
    sample_sentence = "Hello, World! Hello Python Programming."
    
    result_set = find_repeated_letters(sample_sentence)
    
    if not result_set:
        print("No repeated letters found.")
    else:
        # Sort and display results for neatness (e.g., alphabetical order).
        sorted_result = sorted(result_set, key=ord) 
        print(f"Repeated letters in '{sample_sentence}': {', '.join(sorted_result)}")