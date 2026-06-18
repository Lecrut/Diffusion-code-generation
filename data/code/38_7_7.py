def find_duplicate_letters(s: str) -> list[str]:
    """
    Returns a list of all unique letters that appear at least twice in the string,
    handling case-insensitivity by treating 'A' and 'a' as the same letter.
    
    Args:
        s (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of uppercase unique characters found more than once.
    """
    # Convert string to lowercase for case-insensitive comparison
    lower_s = s.lower()
    
    # Dictionary to count occurrences of each letter (ignoring non-alphabetic characters)
    char_count = {}
    
    for char in lower_s:
        if 'a' <= char <= 'z':  # Only consider alphabetic characters
            char_count[char] = char_count.get(char, 0) + 1
            
    # Filter letters that appear at least twice and collect them as uppercase strings
    duplicates = [char for char in sorted(char_count.keys()) if char_count[char] >= 2]
    
    return duplicates

if __name__ == '__main__':
    sample_strings = ["Hello, World!", "AaBbCc", "Programming is fun!!"]
    
    print("Input: 'Hello, World!'")
    result1 = find_duplicate_letters(sample_strings[0])
    print(f"Output: {result1}")
    
    print("\nInput: 'AaBbCc'")
    result2 = find_duplicate_letters(sample_strings[1])
    print(f"Output: {result2}")
    
    print("\nInput: 'Programming is fun!!'")
    result3 = find_duplicate_letters(sample_strings[2])
    print(f"Output: {result3}")