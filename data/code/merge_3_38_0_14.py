def find_repeated_letters(text: str) -> list[str]:
    """
    Identifies letters that appear more than once in the input string, 
    ignoring case and non-alphabetic characters. Returns a sorted list of unique repeated letters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of uppercase repeated letters found.
    """
    letter_counts = {}

    # Iterate over each character in the string
    for char in text:
        if char.isalpha():  # Only consider alphabetic characters
            normalized_char = char.upper()
            letter_counts[normalized_char] = letter_counts.get(normalized_char, 0) + 1

    repeated_letters = []
    
    # Check which letters have a count greater than one and add to the list if not already present
    for letter in sorted(letter_counts.keys()):
        if letter_counts[letter] > 1:
            repeated_letters.append(letter)

    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, stdin, or args)
    samples = [
        "Hello World!",
        "Python Programming",
        "aabbccdd1234",
        "The quick brown fox jumps over the lazy dog.",
        "No repeats here"
    ]

    print("Repeated letters found in sample strings:")
    for text in samples:
        result = find_repeated_letters(text)
        if result:
            repeated_str = "".join(result).upper()
            print(f"'{text}' -> Repeated letters: {repeated_str}")
        else:
            print(f"'{text}' -> No repeated letters found")