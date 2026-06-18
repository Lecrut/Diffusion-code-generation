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
    
    count_map = {}
    
    # Count frequency of each character
    for char in lower_s:
        if not char.isalpha():  # Only consider alphabetic characters
            continue
        count_map[char] = count_map.get(char, 0) + 1
    
    # Collect letters with count >= 2 and convert to uppercase
    duplicates = [char.upper() for char, count in count_map.items() if count >= 2]
    
    return sorted(duplicates)

if __name__ == '__main__':
    sample_strings = ["Hello World!", "AaBbCC", "Python3.9"]
    
    print("Input: 'Hello World!'")
    result1 = find_duplicate_letters(sample_strings[0])
    print(f"Duplicate letters: {result1}")
    
    print("\nInput: 'AaBbCC'")
    result2 = find_duplicate_letters(sample_strings[1])
    print(f"Duplicate letters: {result2}")
    
    print("\nInput: 'Python3.9'")
    result3 = find_duplicate_letters(sample_strings[2])
    print(f"Duplicate letters: {result3}")