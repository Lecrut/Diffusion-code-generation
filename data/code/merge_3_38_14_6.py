def process_string(s: str) -> dict[str, int]:
    """
    Processes a string to find letters that appear more than once.
    
    Args:
        s (str): The input string containing characters.
        
    Returns:
        dict[str, int]: A dictionary where keys are repeated letters 
                        and values are their occurrence counts in the original string.
    """
    letter_counts = {}
    
    for char in s:
        if 'a' <= char.lower() <= 'z':  # Only consider alphabetic characters (case-insensitive)
            lower_char = char.lower()
            letter_counts[lower_char] = letter_counts.get(lower_char, 0) + 1
            
    repeated_letters = {letter: count for letter, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    sample_string = "Hello, World! This is a test. Aaa bb cc dd ee ff gg hh ii jj kk ll mm nn oo pp qq rr ss tt uu vv ww xx yy zz"
    
    result = process_string(sample_string)
    
    print("Repeated letters and their counts:")
    for letter in sorted(result.keys()):
        print(f"{letter}: {result[letter]}")