def process_string(s: str) -> dict[str, int]:
    """
    Processes a string to find repeated letters and their counts.
    
    Only alphabetic characters (a-z, A-Z) are considered. Case-insensitive matching 
    is used for identification but the count reflects total occurrences of that letter 
    regardless of case. The key in the returned dictionary will be lowercase.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        dict[str, int]: A dictionary where keys are repeated letters (lowercase) 
                        and values are their occurrence counts. Only includes letters 
                        that appear more than once in the original string.
    """
    # Convert string to lowercase for case-insensitive processing
    s_lower = s.lower()
    
    letter_counts = {}
    
    # Count occurrences of each alphabetic character
    for char in s_lower:
        if 'a' <= char <= 'z':
            letter_counts[char] = letter_counts.get(char, 0) + 1
    
    # Filter to only include letters that are repeated (count > 1)
    result = {letter: count for letter, count in letter_counts.items() if count > 1}
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or network access is used here.
    sample_string = "Hello World! This string has repeated letters like 'l', 'o', and 'h'."
    
    output_dict = process_string(sample_string)
    
    print("Input String:", sample_string)
    print("\nRepeated Letters Count:")
    for letter, count in sorted(output_dict.items()):
        print(f"  '{letter}': {count}")