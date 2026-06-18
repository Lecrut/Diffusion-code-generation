def find_repeated_letters(text: str) -> list[str]:
    """
    Identifies all letters that appear more than once in the input string.
    
    The function is case-insensitive, treating 'A' and 'a' as the same letter.
    Non-alphabetic characters are ignored during counting but do not affect 
    which letters are reported to be repeated.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of unique alphabetic characters that appear more than once, in lowercase.
    """
    letter_counts = {}

    # Iterate through each character in the string
    for char in text:
        if char.isalpha():  # Only consider alphabetic characters
            lower_char = char.lower()
            letter_counts[lower_char] = letter_counts.get(lower_char, 0) + 1

    # Collect letters with a count greater than one and sort them alphabetically
    repeated_letters = sorted([letter for letter, count in letter_counts.items() if count > 1])

    return repeated_letters

if __name__ == '__main__':
    sample_text = "Hello World! This is a test string. Aaa..."
    
    # Find and print the results directly without user input prompts
    result = find_repeated_letters(sample_text)
    
    if not result:
        print("No repeated letters found.")
    else:
        print(f"Repeated letters in '{sample_text}':")
        for letter in result:
            count = sum(1 for c in sample_text if c.lower() == letter and c.isalpha())
            # Count occurrences specifically to show how many times they repeat (optional detail)
            freq_info = f"{letter}: {count} occurrence(s)"
            print(f"  - {freq_info}")