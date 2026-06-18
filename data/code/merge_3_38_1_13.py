def find_repeated_letters(text: str) -> set:
    """
    Returns a set of letters that appear more than once in the input string.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        set: A set containing all unique characters from 'a'-'z' and 'A'-'Z' 
             that occur more than once, converted to lowercase for consistency.
    """
    letter_counts = {}
    
    # Count occurrences of each character (case-insensitive)
    for char in text.lower():
        if char.isalpha():  # Only consider alphabetic characters
            letter_counts[char] = letter_counts.get(char, 0) + 1
            
    repeated_letters = set()
    
    # Collect letters with count > 1
    for letter, count in letter_counts.items():
        if count > 1:
            repeated_letters.add(letter)
            
    return repeated_letters

if __name__ == '__main__':
    sample_input_1 = "hello world"
    result_1 = find_repeated_letters(sample_input_1)
    
    sample_input_2 = "aabbccddeeffgghhiiijjjkkllmmnnooppqqrrssttuuvvwwxxyyzzzZZZ"
    result_2 = find_repeated_letters(sample_input_2)
    
    print(f"Input: '{sample_input_1}'")
    print(f"Repeated letters: {result_1}")
    print()
    print(f"Input: '{sample_input_2}'")
    print(f"Repeated letters: {sorted(result_2)}")