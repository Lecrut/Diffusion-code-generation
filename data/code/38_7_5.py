def find_duplicate_letters(s: str) -> list[str]:
    """
    Returns a sorted list of unique letters that appear at least twice in the string,
    handling case-insensitivity by treating 'A' and 'a' as the same letter.
    
    Args:
        s (str): The input string to analyze.
        
    Returns:
        List[str]: A sorted list of uppercase letters found more than once.
    """
    # Convert string to lowercase for case-insensitive comparison
    lower_s = s.lower()
    
    letter_count = {}
    
    # Count occurrences of each letter (ignoring non-alphabetic characters)
    for char in lower_s:
        if 'a' <= char <= 'z':
            letter_count[char] = letter_count.get(char, 0) + 1
            
    # Collect letters with count >= 2 and convert to uppercase
    duplicates = [char.upper() for char, count in letter_count.items() if count >= 2]
    
    return sorted(duplicates)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    test_cases = [
        "Hello World!",
        "A man, a plan, a canal: Panama",
        "Programming is fun!!",
        "1234567890 !@#",  # Expected empty list as no letters appear twice
        "aaBBccDDeeFFggHHiiJJkkLLmmNNooPPqqRRssTTuuVVwwXXyyZZ"  # All pairs present
    ]

    for test_string in test_cases:
        result = find_duplicate_letters(test_string)
        print(f"Input: '{test_string}'")
        print(f"Duplicates: {result}")
        print("-" * 30)