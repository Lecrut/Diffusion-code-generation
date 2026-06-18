def find_repeated_letters(text: str) -> list[str]:
    """
    Identifies any repeated letters in a given string, ignoring case.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of unique characters that appear more than once.
                   If no repetitions are found, returns an empty list.
    """
    letter_counts = {}

    # Iterate through each character in the string
    for char in text:
        # Only process alphabetic characters (A-Z and a-z)
        if 'a' <= char.lower() <= 'z':
            lower_char = char.lower()  # Normalize to lowercase for case-insensitive comparison
            
            letter_counts[lower_char] = letter_counts.get(lower_char, 0) + 1

    repeated_letters = []

    # Collect letters that have a count greater than one
    for letter in letter_counts:
        if letter_counts[letter] > 1:
            repeated_letters.append(letter)

    return sorted(repeated_letters)

if __name__ == '__main__':
    sample_text = "Hello, World! This is an example with repeated letters like 'l' and 'e', but also unique ones."
    
    result = find_repeated_letters(sample_text)
    
    if not result:
        print("No repeated letters found.")
    else:
        print(f"Repeated letters in the input string: {result}")