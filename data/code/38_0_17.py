"""
Script to find repeated letters in a given string.
This script checks if any letter appears more than once, ignoring case sensitivity.
It prints each unique repeated letter found exactly once per line.
"""

def find_repeated_letters(text: str) -> list[str]:
    """
    Identifies all unique letters that appear more than once in the input string.

    Args:
        text (str): The input string to analyze.

    Returns:
        List of strings, where each element is a repeated letter found.
    """
    # Dictionary to store character counts
    char_counts = {}

    # Iterate over each character in the string
    for char in text.lower():  # Convert to lowercase for case-insensitive comparison
        if 'a' <= char <= 'z':  # Ensure we only consider alphabetic letters
            char_counts[char] = char_counts.get(char, 0) + 1

    # Extract characters that have a count greater than 1 and sort them alphabetically
    repeated_letters = [char for char, count in char_counts.items() if count > 1]
    return sorted(list(set(repeated_letters)))

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    test_cases = ["Hello World", "Python Programming", "aabbccdd"]

    for text in test_cases:
        print(f"Analyzing string: '{text}'")
        repeated_letters = find_repeated_letters(text)
        
        if not repeated_letters:
            print("No repeated letters found.")
        else:
            # Print the unique repeated letters separated by commas or spaces as needed.
            # Here we join them with a space for readability.
            result_string = " ".join(repeated_letters)
            print(f"Repeated letters found: {result_string}")
        
        print("-" * 40)