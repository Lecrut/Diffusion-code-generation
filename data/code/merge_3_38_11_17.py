def find_repeated_letters(text: str) -> set:
    """
    Returns a set of letters that appear more than once in the input string.
    
    This function uses a dictionary to count occurrences, which is O(n),
    and then filters those with counts greater than 1. It considers only alphabetic
    characters (both cases) but treats 'A' and 'a' as distinct unless specified otherwise;
    here we assume case-sensitive matching based on standard letter definitions.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        set: A set of letters that appear more than once in the string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    letter_counts = {}
    
    # Iterate through each character in the input string
    for char in text:
        if char.isalpha():  # Ensure only alphabetic characters are considered
            current_count = letter_counts.get(char, 0) + 1
            letter_counts[char] = current_count

    # Extract letters with a count greater than one and return as set
    repeated_letters = {letter for letter, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    sample_strings = [
        "aabbcc",
        "Hello World!",
        "Python Programming",
        "",
        "aaaaabbbccc"
    ]

    for test_str in sample_strings:
        result = find_repeated_letters(test_str)
        print(f"Input: '{test_str}' -> Output: {result}")