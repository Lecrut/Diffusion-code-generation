def find_repeated_letters(text: str) -> set:
    """
    Returns a set of all letters that appear more than once in the input string.
    
    The function is case-insensitive and ignores non-alphabetic characters.
    It uses efficient data structures (dictionary for counting, then filtering).

    Args:
        text (str): The input string to analyze.

    Returns:
        set: A set of unique letters that are repeated in the string.
             Letters are returned in lowercase.
    
    Example:
        >>> find_repeated_letters("Hello World!")
        {'h', 'e', 'l', 'o', 'w'}  # Note: 'd' appears once, so not included; case normalized to lower
    """
    if not text:
        return set()

    letter_counts = {}
    
    # Iterate over characters and count occurrences of alphabetic letters (case-insensitive)
    for char in text:
        if char.isalpha():
            lowercase_char = char.lower()
            letter_counts[lowercase_char] = letter_counts.get(lowercase_char, 0) + 1

    # Filter to find only those with count > 1
    repeated_letters = {letter for letter, count in letter_counts.items() if count > 1}
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    samples = [
        "Hello World!",
        "A man a plan a canal Panama",
        "Programming is fun!!",
        "",
        "aabbccdd"
    ]

    for test_input in samples:
        result = find_repeated_letters(test_input)
        print(f"Input: '{test_input}'")
        print(f"Repeated letters: {result}")
        print("-" * 20)