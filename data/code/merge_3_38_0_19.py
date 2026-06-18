def find_repeated_letters(text: str) -> list[str]:
    """
    Identifies letters that appear more than once in the input string, 
    ignoring case sensitivity but preserving original casing if needed (though output is lowercase).
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of unique repeated letters found in the string.
    """
    letter_counts = {}

    # Iterate over each character in the string, skipping non-alphabetic characters
    for char in text:
        if 'a' <= char.lower() <= 'z':  # Check if it's an alphabetic character
            lower_char = char.lower()
            letter_counts[lower_char] = letter_counts.get(lower_char, 0) + 1

    # Extract letters with a count greater than one and sort them for consistent output
    repeated_letters = sorted([letter for letter, count in letter_counts.items() if count > 1])
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    test_cases = [
        "Hello World!",
        "Python Programming",
        "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz",
        "NoRepeatsHere123!",
        "Mississippi"
    ]

    print("Repeated letters found in the following strings:")
    for test_string in test_cases:
        result = find_repeated_letters(test_string)
        if not result:
            print(f"'{test_string}': None")
        else:
            # Format output as a comma-separated string of uppercase letters for readability
            formatted_result = ", ".join([letter.upper() for letter in result])
            print(f"'{test_string}': {formatted_result}")