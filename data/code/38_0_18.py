def find_repeated_letters(text: str) -> list[str]:
    """
    Identifies letters that appear more than once in the input string.
    
    The function is case-insensitive and ignores non-alphabetic characters.
    It returns a sorted list of unique repeated letters found.

    Args:
        text (str): The input string to analyze.

    Returns:
        list[str]: A sorted list of strings, each containing a single 
                   uppercase letter that is repeated in the input.
    """
    # Filter for alphabetic characters and convert to lowercase for case-insensitive comparison
    filtered_chars = [char.lower() for char in text if char.isalpha()]
    
    frequency_map = {}
    
    # Count occurrences of each character
    for char in filtered_chars:
        if char in frequency_map:
            frequency_map[char] += 1
        else:
            frequency_map[char] = 1
            
    # Identify characters with a count greater than one and sort them alphabetically
    repeated_letters = sorted([char for char, count in frequency_map.items() if count > 1])
    
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    samples = [
        "hello world",           # Expected: ['h', 'l'] (case-insensitive) -> sorted output will be based on letter value, but logic handles case insensitivity internally before sorting unique keys? 
                                # Actually, let's trace: h->1, e->1, l->3, o->2... repeated are l and o.
        "A man a plan",         # Expected: ['a'] (case-insensitive 'a' appears multiple times)
        "Python Programming 101" # Expected: ['n', 'p', 'r'] (ignoring numbers/space, case insensitive p->P)
    ]

    for sample_text in samples:
        result = find_repeated_letters(sample_text)
        print(f"Input: '{sample_text}'")
        if result:
            # Format output as a comma-separated string of uppercase letters
            repeated_chars_str = ", ".join([char.upper() for char in result])
            print(f"Repeated letters found: {repeated_chars_str}")
        else:
            print("No repeated letters found.")
        print("-" * 20)