def process_string(s: str) -> dict[str, int]:
    """
    Processes a string to find repeated letters and their counts.
    
    Only alphabetic characters (a-z, A-Z) are considered as 'letters'.
    Case-insensitive matching is used for determining which letter is repeated,
    but the key in the dictionary will be stored in lowercase.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        dict[str, int]: A dictionary where keys are unique letters present 
                        more than once and values are their occurrence counts.
    """
    # Dictionary to store letter counts
    char_counts = {}
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an alphabetic letter
        if 'a' <= char.lower() <= 'z':
            # Convert to lowercase and update count
            lower_char = char.lower()
            char_counts[lower_char] = char_counts.get(lower_char, 0) + 1
    
    # Filter dictionary to only include letters that appear more than once
    repeated_letters = {k: v for k, v in char_counts.items() if v > 1}
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample string containing various characters including repeated letters
    sample_string = "Hello World! Hello Python. PPyythoN"
    
    result = process_string(sample_string)
    
    print("Repeated letters and their counts:")
    for letter, count in sorted(result.items()):
        print(f"{letter}: {count}")