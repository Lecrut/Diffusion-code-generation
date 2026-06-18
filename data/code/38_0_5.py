import string

def find_repeated_letters(text: str) -> list[str]:
    """
    Identifies letters that appear more than once in the input string.
    
    The function is case-insensitive and ignores non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of unique repeated letters found, 
                   represented by their lowercase form. If no repeats are found, returns an empty list.
    """
    # Filter for alphabetic characters and convert to lowercase for case-insensitive comparison
    filtered_chars = [char.lower() for char in text if char.isalpha()]
    
    letter_counts: dict[str, int] = {}
    
    # Count occurrences of each character
    for char in filtered_chars:
        letter_counts[char] = letter_counts.get(char, 0) + 1
    
    # Extract letters with a count greater than one and sort them alphabetically
    repeated_letters = sorted([char for char, count in letter_counts.items() if count > 1])
    
    return repeated_letters

if __name__ == '__main__':
    sample_strings = [
        "Hello World!",
        "Python Programming",
        "aabbccdd",
        "The quick brown fox jumps over the lazy dog.",
        "No repeats here"
    ]

    for test_input in sample_strings:
        result = find_repeated_letters(test_input)
        if not result:
            print(f"No repeated letters found in '{test_input}'")
        else:
            # Print each letter on a new line as per common robust output practices, 
            # or joined by space. Here we join for clarity but could be modified to list format.
            print(f"Repeated letters in '{test_input}': {', '.join(result)}")