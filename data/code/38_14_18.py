def process_string(s: str) -> dict[str, int]:
    """
    Processes a string to find repeated letters (case-insensitive).
    
    Args:
        s (str): The input string to analyze.
        
    Returns:
        dict[str, int]: A dictionary where keys are unique letters 
                        that appear more than once in the string, 
                        and values are their occurrence counts.
    """
    # Initialize a dictionary with all characters from 'a'-'z' having 0 count
    char_counts = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    
    # Iterate through each character in the string, convert to lowercase, and increment its count if it exists in our map
    for char in s:
        lower_char = char.lower()
        if lower_char in char_counts:
            char_counts[lower_char] += 1
    
    # Filter out characters that did not appear more than once (count == 0)
    repeated_letters = {char: count for char, count in char_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    sample_string = "Hello World!"
    result = process_string(sample_string)
    print(result)