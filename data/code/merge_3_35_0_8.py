def count_vowels(text: str) -> int:
    """
    Counts the total number of vowels (a, e, i, o, u) in a string, 
    case-insensitive.

    Args:
        text (str): The input string to analyze.

    Returns:
        int: The count of vowels found in the string.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies
    samples = [
        "Hello, World!",
        "Python Programming",
        "",
        "aeiouAEIOU"
    ]

    for text in samples:
        count = count_vowels(text)
        print(f"'{text}' -> {count} vowels")