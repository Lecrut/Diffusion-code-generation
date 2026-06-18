import string

def find_repeated_letters(text: str) -> dict[str, int]:
    """
    Identifies all letters in the input string that appear more than once.
    
    The function is case-insensitive and ignores non-letter characters (digits, 
    punctuation, whitespace). It returns a dictionary mapping each repeated letter 
    to its total count of occurrences in the text. Only letters present more than 
    once are included in the returned dictionary.

    Args:
        text (str): The input string to analyze.

    Returns:
        dict[str, int]: A dictionary where keys are uppercase letters found multiple times
                        and values represent their occurrence counts. If no repeated letters
                        exist, returns an empty dictionary.
    """
    # Initialize a frequency map for lowercase English alphabets only
    char_count = {}

    # Iterate over each character in the input string
    for char in text:
        if char.isalpha():  # Ensure we only consider actual letters
            lower_char = char.lower()
            char_count[lower_char] = char_count.get(lower_char, 0) + 1
    
    # Filter to keep only those characters that appear more than once and convert keys to uppercase
    repeated_letters = {}
    for letter in string.ascii_lowercase:
        if char_count.get(letter, 0) > 1:
            repeated_letters[letter.upper()] = char_count[letter]

    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    sample_texts = [
        "Hello, World! Hello again.",  # 'H' and 'e' should be detected (case-insensitive)
        "The quick brown fox jumps over a lazy dog."   # No repeated letters expected here
    ]

    print("Analysis of Repeated Letters\n")
    
    for test_text in sample_texts:
        result = find_repeated_letters(test_text)
        
        if not result:
            print(f"Input: '{test_text}'")
            print("Result: No repeated letters found.")
            continue
            
        # Display the results sorted by letter index (A-Z) for better readability
        sorted_result = {k: v for k, v in sorted(result.items())}

        print(f"Input: \"{test_text}\"")
        print(f"Repeated letters and their counts:")
        
        if result:  # Only iterate if there are results to avoid empty loops in logic flow (optional cosmetic improvement)
            for letter, count in sorted_result.items():
                marker = " | "
                full_marker_str = f"{marker}{letter}({count})"
                print(f"  {full_marker_str}")

        # Show summary line after each block of repeated letters or when empty but not None logic (optional)
        if result:
            count_summary_text = len(result) + " letter(s)"
        else:
            count_summary_text = ""

        print()