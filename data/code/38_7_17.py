def find_duplicate_letters(text: str) -> list[str]:
    """
    Returns a sorted list of unique letters that appear at least twice in the input string,
    handling case-insensitivity (e.g., 'A' and 'a' are treated as the same).

    Args:
        text (str): The input string to analyze.

    Returns:
        List[str]: A sorted list of uppercase unique letters found more than once.
    """
    if not text:
        return []

    # Convert to lowercase for case-insensitive comparison and count occurrences
    char_counts = {}
    
    for char in text.lower():
        if 'a' <= char <= 'z':  # Ensure only alphabetic characters are considered
            char_counts[char] = char_counts.get(char, 0) + 1

    # Filter letters that appear at least twice and return them sorted
    duplicates = [char for char, count in char_counts.items() if count >= 2]
    
    return sorted(duplicates)

if __name__ == '__main__':
    sample_strings = ["Hello World!", "A man a plan a canal Panama", "Python Programming"]

    print("Sample Input/Output:")
    for s in sample_strings:
        result = find_duplicate_letters(s)
        if not result:
            print(f"'{s}' -> No duplicate letters found.")
        else:
            # Convert list to string representation for cleaner output (e.g., ['h', 'o'])
            formatted_result = "[" + ", ".join(result) + "]"
            print(f"Input: '{s}'")
            print(f"Duplicates: {formatted_result}")