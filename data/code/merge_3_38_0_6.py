def find_repeated_letters(text: str) -> list[str]:
    """
    Identifies letters that appear more than once in the input string, 
    ignoring case sensitivity but preserving original casing logic if needed.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of unique repeated lowercase letters found.
    """
    letter_counts = {}

    # Iterate over each character in the string
    for char in text:
        if 'a' <= char.lower() <= 'z':  # Ensure we only consider alphabetic characters
            lower_char = char.lower()
            letter_counts[lower_char] = letter_counts.get(lower_char, 0) + 1

    repeated_letters = []
    
    # Check counts and collect letters that appear more than once
    for letter in sorted(letter_counts.keys()):
        if letter_counts[letter] > 1:
            repeated_letters.append(letter)

    return repeated_letters

if __name__ == '__main__':
    sample_string = "Hello, World! This is a test string with repeated letters like 'a' and 'e'. The word 'level' has many repeats."
    
    result = find_repeated_letters(sample_string)
    
    if not result:
        print("No repeated letters found.")
    else:
        print(f"Repeated letters found in the input:")
        for letter in result:
            count = sample_string.lower().count(letter)
            print(f"'{letter}' appears {count} times")