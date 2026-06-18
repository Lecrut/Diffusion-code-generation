def find_repeated_letters(text: str) -> list[str]:
    """
    Identifies letters that appear more than once in the input string.
    
    The function is case-insensitive and ignores non-alphabetic characters.
    It returns a sorted list of unique repeated letters found.

    Args:
        text (str): The input string to analyze.

    Returns:
        list[str]: A sorted list of uppercase letters that are repeated in the input.
    """
    # Filter for alphabetic characters and convert to lowercase for case-insensitive comparison
    filtered_chars = [char.lower() for char in text if char.isalpha()]
    
    frequency_map = {}
    for char in filtered_chars:
        frequency_map[char] = frequency_map.get(char, 0) + 1
    
    # Collect letters with a count greater than 1 and sort them alphabetically
    repeated_letters = sorted([char for char, count in frequency_map.items() if count > 1])
    
    return repeated_letters

if __name__ == '__main__':
    sample_strings = [
        "Hello World!",
        "Python Programming",
        "aabbccdd",
        "The quick brown fox jumps over the lazy dog.",
        "No repeats here"
    ]

    for test_string in sample_strings:
        result = find_repeated_letters(test_string)
        if result:
            print(f"In '{test_string}': Repeated letters are {', '.join(result)}")
        else:
            print(f"In '{test_string}': No repeated letters found.")