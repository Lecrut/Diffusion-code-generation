def find_repeated_letters(sentence: str) -> set[str]:
    """
    Identifies all letters that appear more than once in the given sentence.
    
    The function is case-insensitive and ignores non-alphabetic characters (spaces, 
    punctuation, numbers). It returns a set of lowercase unique repeated letters.
    
    Args:
        sentence (str): The input string to analyze.
        
    Returns:
        set[str]: A set containing the repeated letters in uppercase or lowercase format.
                   We will choose lowercase for consistency but can be adapted easily.
    """
    # Normalize text and filter only alphabetic characters, converting to lower case
    filtered_chars = [char.lower() for char in sentence if char.isalpha()]
    
    letter_counts: dict[str, int] = {}
    
    # Iterate through each character in the filtered list to count occurrences
    for letter in filtered_chars:
        current_count = letter_counts.get(letter, 0) + 1
        letter_counts[letter] = current_count

    # Identify letters with a count greater than one (repeated), store them in a set
    repeated_letters = {letter for letter, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    sample_sentence: str = "Hello World! Python is great and python works well."

    # Hard-coded sample values to test without user input.
    repeated_letter_set = find_repeated_letters(sample_sentence)
    
    print(f"Input sentence: {sample_sentence}")
    print("Repeated letters found:", sorted(repeated_letter_set))