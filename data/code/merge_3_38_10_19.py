def find_repeated_letters(text: str) -> list[str]:
    """
    Identifies all letters that appear more than once in the input string.
    
    The function is case-insensitive and ignores non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of unique repeated letters found, 
                   converted to lowercase for consistency.
    """
    letter_counts = {}

    # Iterate over each character in the string
    for char in text.lower():  # Convert to lower case immediately
        if 'a' <= char <= 'z':  # Ensure it's a letter
            letter_counts[char] = letter_counts.get(char, 0) + 1
    
    repeated_letters = []

    # Check counts and collect letters with frequency > 1
    for letter in sorted(letter_counts.keys()):
        if letter_counts[letter] > 1:
            repeated_letters.append(letter)
    
    return repeated_letters

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "Python Programming",
        "A man a plan a canal Panama",
        "The quick brown fox jumps over the lazy dog"
    ]

    for test_input in sample_strings:
        result = find_repeated_letters(test_input)
        if not result:
            print(f"No repeated letters found in '{test_input}'")
        else:
            # Join with comma and space for readability, e.g., "a, d"
            output_str = ", ".join(result)
            print(f"In '{test_input}': Repeated letters are {output_str}")