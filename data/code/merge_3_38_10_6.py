import string

def find_repeated_letters(text: str) -> list[str]:
    """
    Identifies all letters that appear more than once in the input text, 
    regardless of case sensitivity (e.g., 'A' and 'a' are treated as the same).
    
    Args:
        text (str): The string to analyze.
        
    Returns:
        list[str]: A sorted list of unique repeated letters found.
    """
    # Filter for alphabetic characters only, convert to lowercase for case-insensitive comparison
    filtered_chars = [char.lower() for char in text if char.isalpha()]
    
    letter_counts = {}
    for char in filtered_chars:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
            
    # Collect letters with a count greater than 1 and sort them alphabetically
    repeated_letters = sorted([letter for letter, count in letter_counts.items() if count > 1])
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies
    samples = [
        "Hello World",           # Expected: ['h', 'l', 'o'] (case-insensitive)
        "Programming in Python"  # Expected: ['g', 'n', 'p', 'r', 't', 'y']
    ]

    for sample_text in samples:
        result = find_repeated_letters(sample_text)
        print(f"In '{sample_text}': Repeated letters are {result}")