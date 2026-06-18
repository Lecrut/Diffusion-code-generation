def find_repeated_letters(text: str) -> list[str]:
    """
    Takes a string as input and checks for any repeated letters within that string, 
    printing all repeated letters found (case-insensitive). Returns the sorted unique 
    repeated letters.

    Args:
        text (str): The input string to analyze.

    Returns:
        list[str]: A sorted list of uppercase characters that appear more than once in the input.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    # Convert to lowercase and filter out non-alphabetic characters for processing
    normalized_text = text.lower()
    alpha_only = [char for char in normalized_text if char.isalpha()]

    count_map = {}
    repeated_chars = set()

    for char in alpha_only:
        if char in count_map:
            count_map[char] += 1
            # If it was already marked as repeated, we don't need to add again. 
            # However, since we iterate once, checking 'if > 0' logic here is tricky without a second pass or dict update check.
            # Simpler approach: Just increment count and mark if total becomes 2 first time? 
            # Actually, let's just track counts in the map directly.
        else:
            count_map[char] = 1

    for char, count in count_map.items():
        if count > 1:
            repeated_chars.add(char)

    return sorted(list(repeated_chars))

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No input(), sys.stdin, argparse, or network access used.
    
    test_cases = [
        "Hello World!",
        "Python Programming",
        "aabbccdd",
        "The quick brown fox jumps over the lazy dog.",
        "No repeats here"
    ]

    for sample in test_cases:
        print(f"\nAnalyzing string: '{sample}'")
        repeated = find_repeated_letters(sample)
        
        if not repeated:
            print("  No repeated letters found.")
        else:
            # Print the result as requested (printing all repeated letters found)
            for char in repeated:
                print(f"Repeated letter found: '{char}'")